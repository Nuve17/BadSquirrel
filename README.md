# BadSquirrel

          !!!                    
         !!!!!                   
       !!!!!!!!                  
      !!!!!!!!!!!   O_O          
      !!!  !!!!!!! /@ @\         
            !!!!!! \\ x /        
            !!!!!!/ m  !m        
             !!!!/ __  |         
             !!!!|/  \__         
              !!!\______\       


## Fontionnement
1. Sature toutes les adresses IP du serveur DHCP légitimes (Gateway)  
2. Notre serveur DHCP malveillant propose des adresses IP avec l'option 252 (Web Proxy Auto-Detect) `http://10.0.2.10:7070/wpad.dat`  
3. Le navigateur des victimes se connecte sur notre proxy  
4. Ils sont redirigés sur une page de phishing `rgpd.html`. Cette page leurs propose notre CA `Bad Squirrel CA`.  
5. Une fois la CA importé dans leurs navigateur nous pouvons leurs générer des certificat pour chaque site web consulté.  
6. Sur chaque page avec `Content-type: html/text` nous injectons du JS qui monitore quels clients nous avons infecté.

## Usage
Configuration des machines virtuelle dans [virtualbox_scenario_instructions.md]  
First start run `./setup_https_intercept.sh`   
Launches  the `BadSquirrel.py -i eth0` with root privelege.

### MITM JS Injector
Specify your javascript payload in `payload.js`

### Configuration de DNSMASQ
`cp BadSquirrel/local.conf /etc/dnsmasq.d/`

### Browser with detect WPAD by default

| Browser             | By default    | Manual activation |Tested on |
|--------------------|----------------|---------|---------|
| Internet Explorer  | ✔  | ✖ | ✔ |
| Google Chrome      | ✔  | ✖ | ✔ |
|       Firefox      | ✖  | ✔ | ✖ |
|       Opera        | ✔  | ✖ | ✖ |

Testé sur Windows 7 64 bits
Google Chrome demande a avoir l'authorité de certification en tant que racine mais pas IE

### Monitoring client

Le monitoring se fait via un serveur flask qui écoute sur le port 5000 (le port est configurable dans app.py) et reçoit des informations ci-dessous relatives à chaque client

  ##### Informations du client
  
    - Id
    - Adresse ip
    - Timezone
    - Processeur du client 
    - Useragent
    - OS
    - Site web visité
    





Ces informations sont ensuite vibiles depuis un dashboard accessible à l'adresse sur laquelle le serveur flask écoute
Exemple : http://iplocaleduserveur:5000/dashboard

Pour lancer le serveur de monitorinfg il faut se rendre dans le répertoire "Web", puis lancer :

          # python3 app.py

### Dependencies
Dependencies for Python 2.7 included in `requirements.txt` and can be installed  
using `pip` with `pip install -r requirements.txt`.  
Please update `requirements.txt` when you add new library with `pipreqs /path/to/project`


## TODO
1. Utiliser la page RGPD et pas envoi de `ca.crt` direct
2. Générer des JS malveillant  
3. Choix des différentes Payload
4. Création d'un schema réseau pour l'explication du concept

[virtualbox_scenario_instructions.md]: https://github.com/Nuve17/BadSquirrel/blob/master/virtualbox_scenario_instructions.md  
