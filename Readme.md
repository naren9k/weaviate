# Manage Weaviate on OCP
## Connection to OCP
OCP-Dev new
Web console: [OCP-DEV web console](https://console-openshift-console.apps.dev.ocp.bisinfo.org) 

API:
```bash
oc login https://api.dev.ocp.bisinfo.org:6443
```

Check that you are in the correct project
```commandline
oc project
```
Output should be
```commandline
Using project "data-bisgpt-dev" on server "https://api.dev.ocp.bisinfo.org:6443".
```

If you are on another project, then change to `data-bisgpt-dev`
```commandline
oc project data-bisgpt-dev
```

## Managing PVC
Create, modify the PVC
```commandline
oc apply -f pvc.yml
```

Delete
```commandline
oc delete -f pvc.yml
```

Check that PVC has been created
```commandline
oc get pvc weaviate-data
```

## Managing Keys
Create Key:
First do a dry run to generate the yaml file
```commandline
oc create secret generic my_pass --from-literal=key='{My_password}' -o yaml --dry-run
```

This will generate a yaml file and the password will be encoded with base64, like the following
```yaml
apiVersion: v1
data:
  key: e015X3Bhc3N3b3JkfQ==
kind: Secret
metadata:
  creationTimestamp: null
  name: my_pass
```

You can put the above to a yaml file, e.g. my_pass.yml and then create it
```commandline
oc apply -f my_pass.yml
```

## Deployment phase
1. Deploy pvc and api_key. No need to do that every time, only if there is a change
2. Deploy the deployment
```commandline
oc apply -f deployment.yml
```
3. Deploy the service
```commandline
oc apply -f service.yml
```
4. Deploy the route
```commandline
oc apply -f route.yml
```
5. You are ready!!!


Notes:
* `deployment.yml` : This is defining the `weaviate` instance, image, environment variables etc.
* `service.yml` : Expose the deployment to be accessible from other services in OCP
* `route.yml` : Expose the deployment (service) to anyone externally to OCP. This is also adding the TLS

URL:
| External URL | Redirects to | Comment |
| --- | --- | --- |
| https://weaviate-data-bisgpt-dev.apps.dev.ocp.bisinfo.org/ | weaviate:8080 | Base URL |
| https://weaviate-grpc-data-bisgpt-dev.apps.dev.ocp.bisinfo.org/ | weaviate:5051 | GRPC |


Test REST
```commandline
curl -H @{"Authorization" = "Bearer my_bearer"}  "https://weaviate-data-bisgpt-dev.apps.dev.ocp.bisinfo.org:443/v1/schema"
```
