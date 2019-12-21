# My Academic CV

Academic CV for James Doss-Gollin.
Output is available [here](docs/CV_Doss-Gollin_James.pdf)

## Building

Everything is stored in the `data/` folder in `yml` format, and then is converted to latex using python scripts.
This makes it easy to update the CV without worrying about latex syntax (though there's still a lot of custom latex in the CV latex file).

To create the PDF:

```
make pdf
```

That will build the PDF and put a copy in the `docs/` folder for serving with GitHub pages