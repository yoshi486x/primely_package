# How to update build a new pkg

```bash
python setup.py bdist_wheel
```

A wheel file will be generated in `dist/` folder.

```python
>>> from primely.controller import controller
>>> controller.paycheck_analysis()
```
