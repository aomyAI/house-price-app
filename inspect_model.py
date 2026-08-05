import joblib
import os
from pprint import pprint

path = os.path.join('backend', 'app', 'models', 'house_price_rf_model.pkl')
model = joblib.load(path)
print('type:', type(model))
print('has named_steps:', hasattr(model, 'named_steps'))
if hasattr(model, 'named_steps'):
    pprint(list(model.named_steps.keys()))
print('feature_names_in_:', getattr(model, 'feature_names_in_', None))
print('steps:', getattr(model, 'steps', None))
print('get_feature_names_out:', hasattr(model, 'get_feature_names_out'))
# try to inspect first transformer if possible
try:
    if hasattr(model, 'named_steps'):
        for name, step in model.named_steps.items():
            print('STEP', name, type(step), getattr(step, 'get_params', lambda: None)())
except Exception as e:
    print('inspect error:', e)
