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

### Resources
- [mozilla-django-oidc](https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html) - Link to documentation for the Python library providing the necessary OIDC tooling for Django
- [UM ITS Shibboleth Resources](https://documentation.its.umich.edu/node/287) - Link to information and resources about using ITS-provided Shibboleth
- [UM Shibboleth Well Known](https://shibboleth.umich.edu/.well-known/openid-configuration) - Link to the Shibboleth OIDC metadata for the University of Michigan