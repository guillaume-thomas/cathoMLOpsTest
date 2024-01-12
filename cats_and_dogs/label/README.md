Pour cette étape, nous allons utiliser ecotag. Outil opensource qui permet de faire des labels sur 
des images.

Nous prenons d'abord connaissance du dataset. Ce sont des pdfs avec une image par page.

Nous avons donc une première étape de pre-processing pour transformer les pdfs en image

Nous créons ensuite le projet dans ecotag en local (valider comment le faire dans codespace, 
notamment problèmes de redirections)

Nous obtenons à la fin le résultat du labelling que nous utiliserons dans le train

D'abord, bien builder le package d'extraction (voir le readme), puis pip install des requirements de label

```bash
cd ./cats_and_dogs/label
git clone https://github.com/AxaGuilDEv/ecotag.git
cd ./ecotag
```

Replacer les urls de redirection côté front
exemple : https://potential-spoon-7wj6gp77w542xxp4-5010.app.github.dev/

```yaml
ecotag:
  build:
    context: .
    dockerfile: ./Dockerfile
  environment:
    ASPNETCORE_ENVIRONMENT: Docker
``` 
Remplacer localhost:5010 dans le fichier environment.docker.json
Exemple : 
```json
{
  "apiUrl": "https://potential-spoon-7wj6gp77w542xxp4-5010.app.github.dev/api/server/{path}",
  "baseUrl": "",
  "oidc": {
    "mode": "Default",
    "configuration": {
      "client_id": "interactive.public",
      "redirect_uri": "https://potential-spoon-7wj6gp77w542xxp4-5010.app.github.dev/authentication/callback",
      "silent_redirect_uri": "https://potential-spoon-7wj6gp77w542xxp4-5010.app.github.dev/authentication/silent-callback",
      "scope": "openid profile email api offline_access",
      "authority": "https://demo.duendesoftware.com",
      "service_worker_relative_url": "/OidcServiceWorker.js",
      "service_worker_only": true,
      "token_renew_mode": "access_token_invalid"
    }
  },
  "telemetry": {
    "instrumentationKey": "",
    "logLevel": "DEBUG",
    "active": false
  },
  "datasets": {
    "isBlobTransferActive": false,
    "reserveHttpCallInParallel": 2,
    "reserveBeforeEndIndex": 10
  }
}

```

Ajouter également l'url dans OidcTrustedDomains.docker.js
```js
// Add here trusted domains, access tokens will be send to
const trustedDomains = {
    default: ["http://localhost:5010", "https://demo.duendesoftware.com", "https://didactic-space-bassoon-vwj9xqpp5jjcrpw-5010.app.github.dev"],
    access_token: { domains : ["http://localhost:5010", "https://demo.duendesoftware.com", "https://didactic-space-bassoon-vwj9xqpp5jjcrpw-5010.app.github.dev"], showAccessToken: true }
};
```

Dans StartupServer.cs, remplacer les lignes suivantes : 

```
if (!string.IsNullOrEmpty(corsSettings.Origins))
            services.AddCors(options =>
            {
                options.AddPolicy("CorsPolicy",
                    builder =>
                    {
                        builder
                            .WithOrigins("*")
                            .AllowAnyMethod()
                            .AllowAnyHeader()
                            //.AllowCredentials()
                            .SetPreflightMaxAge(TimeSpan.FromSeconds(2520));
                    });
            });
``` 

```bash
docker compose up -d
cd ../../..
```


Vérifier que tout fonctionne bien sur http://localhost:5010 (ou sur l'url de codespace)

Puis, lancer l'initialisation du projet ecotag : 

```bash
pip install -r ./cats_and_dogs/label/requirements.txt
python ./cats_and_dogs/label/run.py --dataset_folder=./cats_and_dogs/label/dataset --raw_dataset_subfolder=/01_raw --postprocess_dataset_subfolder=/02_postprocess --jwt_token=
```
