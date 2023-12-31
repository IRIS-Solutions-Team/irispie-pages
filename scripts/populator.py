
import irispie as ir
import sys
import os
import re
import yaml
import operator as _op
from loguru import logger
from types import (FunctionType, MethodType, )
from typing import (Callable, )


# with open("mkdocs.yml", "rt", ) as f:
    # mkdocs = yaml.load(f, Loader=yaml.SafeLoader, )
# docs_root = mkdocs["docs_dir"]

docs_root = "docs"

def main():
    klasses = [
        ir.Sequential,
        ir.Simultaneous,
        ir.PlanSimulate,
        ir.PlanSteady,
        ir.Databox,
        ir.Series,
        ir.Dater,
        ir.PlotlyWrapper,
        ir.Chartpack,
        ir.Rephrase,
    ]
    for klass in klasses:
        logger.info(f"Documenting {klass.__name__}...")
        _document_class(klass, )


def _document_class(klass: type, ) -> None:
    """
    """
    klass_path = os.path.join(docs_root, *klass._pages_path, )
    attributes = _collect_documented_attributes_from_class(klass, )
    properties = _collect_documented_properties_from_class(klass, )
    attribute_to_docstring = _create_attribute_to_docstring(attributes, )
    property_to_docstring = _create_attribute_to_docstring(properties, )
    attribute_to_docstring = dict(sorted(
        attribute_to_docstring.items(),
        key=lambda item: item[0]._pages_call_name,
    ))
    docstring = _preprocess_docstring(klass.__doc__, )
    docstring += _create_categorical_list(klass, attribute_to_docstring, )
    docstring += _create_property_list(klass, property_to_docstring, )
    docstring += _add_attributes(attribute_to_docstring, )
    with open(klass_path, "wt+") as f:
        f.write(docstring, )


_ICONS = {
    None: ":octicons-file-24:",
    "property": ":octicons-package-24:",
}
_DIVIDER_PATTERN = re.compile(r"\n·{20,}\n", )
_DIVIDER_PATTERN_LEGACY = re.compile(r"\n\.{20,}\n", )
_PAGES_REFERENCE = "_pages_reference"
_CATEGORY_TABLE_HEADING = (
    "Function | Description\n"
    "----------|------------\n"
)
_PROPERTY_TABLE_HEADING = (
    "Property | Description\n"
    "----------|------------\n"
)


def _preprocess_docstring(docstring: str, ) -> str:
    docstring = _DIVIDER_PATTERN.sub("", docstring)
    docstring = _DIVIDER_PATTERN_LEGACY.sub("", docstring)
    return docstring


def _create_categorical_list(klass: type, attribute_to_docstring: dict, ) -> str:
    docstring = (
        "\n\n\n"
        "Categorical list of functions\n"
        "-------------------------------\n\n"
    )
    for category, category_description in klass._pages_categories.items():
        if category == "property":
            continue
        docstring += f"### {category_description} ###\n\n"
        docstring += _CATEGORY_TABLE_HEADING
        attribute_to_docstring_of_category = _collect_attribute_to_docstring_of_category(attribute_to_docstring, category, )
        for attribute in attribute_to_docstring_of_category.keys():
            icon = _ICONS.get(attribute._pages_category, _ICONS[None], )
            docstring += f"[{icon}`{attribute._pages_call_name}`](#{_get_anchor(attribute._pages_call_name)}) | {attribute._pages_tagline}\n"
        docstring += "\n\n"
    return docstring


def _create_property_list(klass: type, property_to_docstring: dict, ) -> str:
    docstring = (
        "\n\n\n"
        "Directly accessible properties\n"
        "------------------------------\n\n"
    )
    category = "property"
    docstring += _PROPERTY_TABLE_HEADING
    property_to_docstring_of_category = _collect_attribute_to_docstring_of_category(property_to_docstring, category, )
    for property in property_to_docstring_of_category.keys():
        icon = _ICONS.get(property._pages_category, _ICONS[None], )
        docstring += f"[{icon}`{property._pages_call_name}`](#{_get_anchor(property._pages_call_name)}) | {property._pages_tagline}\n"
    docstring += "\n\n"
    return docstring


def _add_attributes(attribute_to_docstring: dict, ) -> None:
        return "\n\n\n".join(
            _finalize_attribute_docstring(a, d, )
            for a, d in attribute_to_docstring.items()
            if a._pages_category != "property"
        )


def _collect_documented_attributes_from_class(klass: type, ) -> list:
    return tuple(
        getattr(klass, attribute_name, )
        for attribute_name in dir(klass)
        if getattr(getattr(klass, attribute_name, ), _PAGES_REFERENCE, False)
    )


def _collect_documented_properties_from_class(klass: type, ) -> list:
    return tuple(
        getattr(klass, attribute_name, ).fget
        for attribute_name in dir(klass)
        if (
            hasattr(getattr(klass, attribute_name, ), "fget")
            and getattr(getattr(klass, attribute_name).fget, _PAGES_REFERENCE, False)
        )
    )


def _create_attribute_to_docstring(references: list, ) -> dict:
    return {
        attribute: _DOCSTRING_EXTRACTOR[type(attribute)](attribute, )
        for attribute in references
    }


def _collect_attribute_to_docstring_of_category(attribute_to_docstring: dict, category: str, ) -> dict:
    return {
        attribute: attribute_docstring
        for attribute, attribute_docstring in attribute_to_docstring.items()
        if attribute._pages_category == category
    }


def _finalize_attribute_docstring(attribute, docstring: str, ) -> str:
    docstring = _preprocess_docstring(docstring, )
    icon = _ICONS.get(attribute._pages_category, _ICONS[None], )
    icon = "&#9744;&nbsp;"
    preface = (
        "\n\n---\n\n"
        f"{icon}`{attribute._pages_call_name}`\n----------------------------------\n\n"
    )
    return preface + docstring


def _get_anchor(call_name: str) -> str:
    return call_name.replace(".", "").lower()


_DOCSTRING_EXTRACTOR = {
    FunctionType: _op.attrgetter("__doc__", ),
    MethodType: _op.attrgetter("__func__.__doc__", ),
}


if __name__ == "__main__":
    main()

