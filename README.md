## django-oidc template

### Set up instructions

#### Configuration

1. Copy the .env.sample file.  
   ```
   cp .env.sample .env
   ```

2. Fill in the empty values.  
    `IDP_ROOT_URL` will be https://shibboleth.umich.edu unless you are using the staging environment 
    in which case it will be https://shib-idp-staging.dsc.umich.edu  
    
   `OIDC_RP_CLIENT_ID` and `OIDC_RP_CLIENT_SECRET` will be shared with you after you submit a 
   [Shibboleth Configuration Request](https://its.umich.edu/accounts-access/shibboleth/configuration-request-form)


#### Using `docker-compose.yml`

1. Build the image.

```
docker-compose build
```

Note: `docker compose build` also works now.

2. Start a container using the image.

```
docker-compose up
```

To stop the container, you can use `^C` and/or `docker-compose down`.

Because `docker-compose.yml` mounts the current directory inside the
container, many changes to source code can be made without re-loading.
Re-builds will be necessary for dependency changes.

#### Using Docker on the command line

1. Build the image.

```
docker build -t starter-django-oidc .
```

2. Start a container using the image.

```
docker run --name starter-django-oidc-cont -p 8000:8000 starter-django-oidc
```

To stop the container, you can use `^C` in the terminal window,
or `docker stop starter-django-oidc-cont`.
