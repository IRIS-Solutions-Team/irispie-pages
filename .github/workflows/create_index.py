
import irispie as ir

files = ['data_management', 'data_management/databoxes', 'data_management/dates', 'data_management/series',
         'data_visualization', 'data_visualization/chartpacks', 'data_visualization/plotly',
         'structural_models', 'structural_models/model_language', 'structural_models/preparser',
         'structural_models/sequential_models', 'structural_models/simulation_plans', 
         'structural_models/simultaneous_models', 'structural_models/steady_plans',
         'time_series_models', 'time_series_models/dynafacts', 'time_series_models/vars']

for i in files:
    f = open('docs/'+i+'/index.md', "wt+")
    f.write(ir._test_docs_.__doc__)