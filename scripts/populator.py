
import irispie as ir
import sys
import os
import re


docs = "docs"
structural_models = os.path.join(docs, "structural_models")
simulation_plans = os.path.join(structural_models, "simulation_plans")



def main():
    klass = ir.PlanSimulate
    klass_folder = simulation_plans

    with open(os.path.join(klass_folder, "index.md", ), "wt+") as f:
        s = _preprocess_docstring(klass.__doc__)
        f.write(s, )

    if hasattr(klass, "_properties"):
        with open(os.path.join(klass_folder, "_properties.md", ), "wt+") as f:
            s = _preprocess_docstring(klass._properties.__doc__)
            f.write(s, )


lead_line_pattern = re.compile(r"^\s*\-+")
trail_line_pattern = re.compile(r"\-+\s*$")


def _preprocess_docstring(docstring: str, ) -> str:
    docstring = lead_line_pattern.sub("", docstring)
    docstring = trail_line_pattern.sub("", docstring)
    return docstring


if __name__ == "__main__":
    main()

