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
Réserve toutes les adresse du DHCP pour proposer un dhcp via DNSMASQ.  
Notre DHCP propose un WPAD.dat sur le 7070 (Web Proxy Auto-Detect).  
Le navigateur de la victime ce connecte a notre proxy.  
A la premiere connexion la victime est redirigée sur notre page `rgpd.html`  
Celle-ci lui propose d'enregistrer notre CA pour garantir la sécurité de ses données.  
Une fois, la CA importer notre victime est compromise Nous avons acces a toutes les données qui transite entre sont navigateur web et l'extérieur.

## Usage
First start run `./setup_https_intercept.sh`   
Launches  the `BadSquirrel.py -i eth0` with root privelege.

### MITM JS Injector
Specify your javascript payload in `inject_js_into_client()`

### Configuration de DNSMASQ
`cp BadSquirrel/local.conf /etc/dnsmasq.d/`


### Dependencies
Dependencies for Python 2.7 included in `requirements.txt` and can be installed  
using `pip` with `pip install -r requirements.txt`.  
Please update `requirements.txt` when you add new library with `pipreqs /path/to/project`


## TODO
Mettre en place le DHCP Starvation  
Fermer de manieres propres le script `KeyboardInterrupt`  
Auto-update du fichier local.conf  
Start/ Stop du DNSMASQ dans `BadSquirrel.py`  
Générer des JS malveillant  
Utilisations possible du plusieurs payload  
