# Newton Polynomial Interpolation

Newton Polynomial Interpolation:

```python
import numpy as np
from newton_polynomial import polynomial

x = np.array((1, 2, 3, 4, 5, 6, 7))
y = np.array((52.5, 34, 13.5, 0, 2.5, 30, 91.5))
p = polynomial(x, y)
print(p)  # 1.5*x**3 - 10.0*x**2 + 1.0*x + 60.0
```

## Tests

Run

    python tests/test.py
