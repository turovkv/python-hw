```
sudo docker build -t gen_latex .
sudo docker run -it --name gen_latex_c -v "$(pwd)/artifacts:/app/artifacts" gen_latex
```
##[pypi repo](https://test.pypi.org/project/astprintfib/0.1.1/)