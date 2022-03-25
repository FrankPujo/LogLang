# LogLang
Language that uses only logic gates.
## Syntax
Each line's purpose is defined by its initial keyword.
| **Keyword** | **Example**             | **Usage**                                                                          |
| ----------- | -----------             | ---------                                                                          |
| **loc**     | *loc variable > 0*      | Define a variable with a value of 0 or 1 (or the result of a function)             |
| **def**     | *def do > a1 ^ a2*      | Define a function using 0, 1 and a1, a2, a3... as variable (call with *do{}*)      |
| **ret**     | *ret var1 var2*         | Return function at the end of the file, can take multiple values                   |
| **inc**     | *inc filename*          | Include all the functions from an external file (library)                          |
| **exp**     | *exp fun1 fun2*         | Export function at the end of library files, can take multiple functions to export |
+ Standard logic gates are *^* (and) and *V* (or). *°* (not) is added at the beginning of a variable name.
