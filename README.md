# python-app-serie

## Comandos
- Crear imagen
    ```console
     $ docker build -t {image-name}:{tag-version} .
    ```

- Crear contenedor
    ```console
     $ docker run -d --name {container-name} -e PYTHONUNBUFFERED=1 {image-name}:{tag-version}
    ``` 