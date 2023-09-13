<div align="center">
    <h1>Résultat de mon analyse de mipcm.com</h1>
</div>

# URL

## Réponses

Dans le cas des requêtes sur les URL finissant en `.js`, la réponse est du javascript (logique !). Pour pouvoir être interprétée, il y a deux options:

- En JavaScript, on peut directement exécuter le contenu du fichier pour peu qu'il existe une fonction message, par exemple :
  
  ```js
  function message(message_json) {
      console.log(message_json)
  }
  ```

- Dans tous les autres cas, on peut extraire le contenu grâce à un peu de manipulation de chaîne de caractères. Par exemple en Python :
  
  ```py
  import re
  import json
  
  def parse_response(response:str) -> dict:
      response_str = re.sub( # re.sub réalise une substitution suivant l'expression régulière
          r"(?P<before_key>[\{\[,])(?P<space_before>\s?)(?P<key>[a-z0-9_\.]+)(?P<after_key>:)(?P<space_after>\s?)", # Expression régulière
          '\\g<before_key>"\\g<key>"\\g<after_key>', # Chaine de substitution
          response[8:-2], # Permet de supprimer `message(` et `);` propre au JS
          0, # Indice de départ
          re.IGNORECASE | re.MULTILINE,
      )
  
      return json.loads(response_str) # Transforme la chaine de caractères en object
  ```
  
    ou en javascript
  
  ```js
  const regexp = /(?<before_key>[\{\[,])(?<space_before>\s?)(?<key>[a-z0-9_\.]+)(?<after_key>:)(?<space_after>\s?)/gim
  const subst = `$<before_key>"$<key>"$<after_key>` 
  
  function parse_message(response) {
      response_string = response
          .substring(8, response.length - 2) // Permet de supprimer `message(` et `);` propre au JS
          .replace(regexp, subst) // Réalise une substitution suivant l'expression régulière
  
      return JSON.parse(response_string) // Transforme la chaine de caractères en object
  }
  ```

## Paramètres génériques

Paramètres appliqués à chaque requête.

- `hfrom_handle` (optionnel) : un entier qui identifie la requête (généralement on incrémente la valeur à chaque requête).
  
    La valeur est renvoyée dans la réponse (`to_handle`).

## (https) www.mipcm.com:7443

### /cmipcgw/cmipcgw_get_req.js

Permet de récupérer la liste des adresses accessibles dont celle concernant l'accès à la caméra.

`https://www.mipcm.com:7443/cmipcgw/cmipcgw_get_req.js`

Exemple de réponse (JSON) :

```json
{
    "type": "cmipcgw_get_ack",
    "from": 272629760,
    "from_handle": 110780813,
    "data": {
        "result": "",
        "server": {
            "signal": ["http://51.255.94.203:7080/ccm", "binnet://51.255.94.203:7001"],
            "debug": "telnet://51.255.94.203:7024",
            "license": "binnet://47.112.212.108:12761",
            "ping": "51.255.94.203",
            "ntp": ["17.253.114.125"],
            "param": [
                { "name": "f_log", "value": "1" },
                { "name": "flog", "value": "all" },
                { "name": "f_scene", "value": "1" },
                { "name": "f_rfdev", "value": "1" },
                { "name": "f_cld", "value": "1" },
                { "name": "f_web", "value": "1" },
                { "name": "sc.iot", "value": "1" },
                { "name": "sc.alexa_link", "value": "enable" },
                { "name": "netdet_url", "value": "http://149.202.201.87:3080/dcm/network_check/url_list/oveu/detect_list.js" },
                { "name": "sc.netcheck.enable", "value": "1" }
            ]
        },
        "myaddr": "{{CLIENT_IP_ADDRESS}}",
        "myloc": "{{COUNTRY_CODE}}",
        "time": 1694456684,
        "timezone": "",
        "ex": ""
    }
}
```

Dans le cas de la caméra, j'ai retenu la valeur `data.server.signal` (ici `http://51.255.94.203:7080/ccm`) qui sert pour toutes les autres requêtes.

Dans les parties suivantes, `IP` et `PORT` désignent respectivement `51.255.94.203` et `7080` dans le cas de cet exemple.

## (http) {{IP}}:{{PORT}}/ccm

`IP` et `PORT` proviennent de la requête [/cmipcgw/cmipcgw_get_req.js](#cmipcgwcmipcgw_get_reqjs) (juste au dessus).

### /mmq_create.js

Permet de créer une session et de récupérer son identifiant.

`http://{{IP}}:{{PORT}}/ccm/mmq_create.js`

Paramètres :

- `hqid` (optionnel) : _Utilisation inconnue_
- `dtimeout` (optionnel) : `30000` _Utilisation inconnue, je n'ai pas vérifié l'expiration de la session après `dtimeout` secondes ou millisecondes_

Exemple de réponse (JSON) :

```json
{ 
    "type": "mmq_create_ack", 
    "from": 270532608, 
    "to_handle": 20, 
    "data": { 
        "result": "", 
        "qid": "2889253143447998" 
    } 
}
```

On récupère la valeur `data.qid` (ici `2889253143447998`), par la suite définit sous le nom `QID`.

En cas d'erreur la valeur `data.result` ne sera pas vide.

### /cacs_dh_req.js

Permet de générer des clés Diffie-Hellman.

`http://{{IP}}:{{PORT}}/ccm/cacs_dh_req.js`

Paramètres :

- `hqid` (optionnel) : [`QID`](#mmq_createjs)

- `dnum_prime` : `791658605174853458830696113306796803` (provient du code source de MIPC : [mdh](/mipc%20source%20code/extract/mdh.js#L434)).

- `droot_num` : `5` (provient du code source de MIPC : [mdh](/mipc%20source%20code/extract/mdh.js#L435)).

- `dkey_a2b` : Clé publique générée par le module [mdh](/mipc%20source%20code/extract/mdh.js#L433)
  
  ```js
  const private = mdh.gen_private()
  const public = mdh.gen_public(private)
  ```
  
    Par la suite la valeur de `private` est désignée par `PRIVATE`.
    Par la suite la valeur de `public` est désignée par `PUBLIC`.

- `dtid` (optionnel) : `0`_Utilisation inconnue_

Exemple de réponse (JSON) :

```json
{
    "type": "cacs_dh_ack",
    "from": 270532608,
    "from_handle": 264519293,
    "to_handle": 21,
    "data": { 
        "result": "", 
        "key_b2a": "145305405769426499099507932653795041", 
        "lid": "0x212fc1", 
        "tid": "0x9640aea", 
        "did": "0x0", 
        "vreq": "" 
    }
}
```

On récupère les valeurs :

- `data.key_b2a` (ici `145305405769426499099507932653795041`), par la suite définit sous le nom `KEY`
- `data.lid` (ici `0x212fc1`), par la suite désignée par `LID`

En cas d'erreur la valeur `data.result` ne sera pas vide.

### /cacs_login_req.js

Permet de s'authentifier auprès du serveur.

`http://{{IP}}:{{PORT}}/ccm/cacs_login_req.js`

Paramètres :

- `hqid` : [`QID`](#mmq_createjs)

- `dlid` : [`LID`](#cacs_dh_reqjs)

- `dnid` : 
    Générée grâce à la fonction `nid` du module [mcodec](/mipc%20source%20code/extract/mcodec.js)
  
  ```js
  mcodec.nid(seq, lid, sharedKey, 2, null, null, md5, "hex")
  ```
  
    où : 
  
  - `seq` : valeur actuelle de la variable à incrémenter ([`hfrom_handle`](#paramètres-génériques))
  
  - `lid` : [`LID`](#cacs_dh_reqjs)
  
  - `sharedKey` : Générée par la fonction `gen_shared_secret` du module [mdh](/mipc%20source%20code/extract/mdh.js#L442)
    
    ```js
    mdh.gen_shared_secret(private, key_b2a)
    ```
    
      où :
    
    - `private` : [`PRIVATE`](#cacs_dh_reqjs)
    - `key_b2a` : [`KEY`](#cacs_dh_reqjs)
    
    Ensuite désignée sous le nom `SHARED_KEY`.
  
  Ensuite donné sous le nom `NID`.

- `duser` : Le nom d'utilisateur ou l'adresse mail

- `dpassword` : Le mot de passe chiffré grâce aux modules `CryptoJS`
  
  ```js
  const encryptedPassword = CryptoJS.DES.encrypt(
      CryptoJS.MD5(password),
      CryptoJS.MD5(sharedKey),
      {
          iv: CryptoJS.enc.Hex.parse("0000000000000000"),
          padding: CryptoJS.pad.NoPadding,
      }
  ).ciphertext.toString()
  ```
  
    où :
  
  - `sharedKey` : Générée ci-dessus
  
  - `password` : Mot de passe en clair

- `dsession_req` (optionnel) : `1` _Utilisation inconnue_

- `dparam__x_countz_` (optionnel) : `2` _Utilisation inconnue_

- `dparam` (optionnel) : `1` _Utilisation inconnue_

- `dparam_name` (optionnel) : `spv` _Utilisation inconnue_

- `dparam_value` (optionnel) : `v1` _Utilisation inconnue_

- `dparam_1` (optionnel) : `1` _Utilisation inconnue_

- `dparam_1_name` (optionnel) : `uctx` _Utilisation inconnue_

- `dparam_1_value` (optionnel) : `data:application/octet-stream;base64,{{encryptedInformations}}` _Utilisation inconnue_
  
    référence dans le code source : [app.420d1150.js:8339](/mipc%20source%20code/website/dcm/version/repo/website/pkg-website-v9.10.1.2210121414/js/app.420d1150.js#L8339), [app.420d1150.js:6745](/mipc%20source%20code/website/dcm/version/repo/website/pkg-website-v9.10.1.2210121414/js/app.420d1150.js#L6745) et [app.420d1150.js:6699](/mipc%20source%20code/website/dcm/version/repo/website/pkg-website-v9.10.1.2210121414/js/app.420d1150.js#L6699)

Exemple de réponse (JSON) :

```json
{
    "type": "cacs_login_ack",
    "from": 270532608,
    "from_handle": 272792949,
    "to_handle": 39,
    "data": {
        "result": "",
        "sid": "0x0",
        "seq": 0,
        "addr": "{{CLIENT_IP}}",
        "loc": "{{COUNTRY_CODE}}",
        "guest": 0,
        "vreq": "",
        "uid": "0x0",
        "lid": "0x0",
        "lkey": ""
    }
}
```

En cas d'erreur la valeur `data.result` ne sera pas vide.

### /ccm_devs_get.js

Fournit une liste des appareils connectés au compte MIPC et quelques informations à leur sujet.

`http://{{IP}}:{{PORT}}/ccm/ccm_devs_get.js`

Paramètres :

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1`

- `dsess_nid` : [`NID`](#cacs_login_reqjs)

- `dstart` : `0` Permet de tronquer la liste par le début (une valeur de `1` permet de ne pas recevoir le premier appareil)

- `dcounts` : `1024` Nombre maximum d'appareil à renvoyer

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_devs_get_ack",
    "from": 270532608,
    "from_handle": 275210133,
    "to_handle": 64,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "start": 0,
        "total": 1,
        "devs": [
            {
                "type": "IPC",
                "stat": "Online",
                "addr": "{{CAMERA_IP}}",
                "authority": "",
                "mfc": "",
                "model": "f136",
                "bimg_ver": "v5.1.8.1807231606",
                "img_ver": "v5.3.1.2003161406",
                "sn": "{{CAMERA_ID}}",
                "dev_id": "{{CAMERA_ID}}",
                "nick": "{{CAMERA_NICKNAME}}",
                "p": [
                    { "n": "p2", "v": "CIF" },
                    { "n": "s.pwdw", "v": "0" },
                    { "n": "sncf", "v": "v1v2" },
                    { "n": "s.new", "v": "1" },
                    { "n": "s.sound_detect", "v": "0" },
                    { "n": "s.noio", "v": "1" },
                    { "n": "s.pic_cloud", "v": "1" },
                    { "n": "s.sys_ok_audio", "v": "1" },
                    { "n": "s.first_config", "v": "1" },
                    { "n": "s.sensor", "v": "ok" },
                    { "n": "s.wifq", "v": "82" },
                    { "n": "s.maxid", "v": "0" },
                    { "n": "s.minid", "v": "1" },
                    { "n": "s.wifs", "v": "srvok" },
                    { "n": "s.eifs", "v": "ifaceok" },
                    { "n": "s.cloud", "v": "1" },
                    { "n": "s.audio_alarm_manually", "v": "1" },
                    { "n": "s.nwlan", "v": "ok" },
                    { "n": "s.nwwan", "v": "null" },
                    { "n": "s.motion_track", "v": "0" },
                    { "n": "s.cmd", "v": "1" },
                    { "n": "s.audio_alarm", "v": "1" },
                    { "n": "s.spv", "v": "1" },
                    { "n": "s.neth", "v": "ok" },
                    { "n": "s.search_by_cid", "v": "1" },
                    { "n": "s.motion", "v": "stop" },
                    { "n": "s.code_match", "v": "1" },
                    { "n": "s.record", "v": "0" },
                    { "n": "s.oscene", "v": "1" },
                    { "n": "s.alert", "v": "0" },
                    { "n": "p0", "v": "HD720p" },
                    { "n": "s.qrc", "v": "no" },
                    { "n": "s.vlose", "v": "0" },
                    { "n": "s.cloud_mul_chn", "v": "1" },
                    { "n": "p1", "v": "D1" },
                    { "n": "dc.p2", "v": "CIF" },
                    { "n": "dc.rf", "v": "1" },
                    { "n": "dc.sncf", "v": "v1v2" },
                    { "n": "dc.bver", "v": "v5.1.8.1807231606" },
                    { "n": "dc.ver", "v": "v5.3.1.2003161406" },
                    { "n": "dc.wfcnr", "v": "2" },
                    { "n": "dc.devtype", "v": "IPC" },
                    { "n": "dc.startsnd", "v": "1" },
                    { "n": "dc.sensor", "v": "ok" },
                    { "n": "dc.cloud", "v": "1" },
                    { "n": "dc.timezone", "v": "2" },
                    { "n": "dc.cmd", "v": "1" },
                    { "n": "dc.spv", "v": "1" },
                    { "n": "dc.oscend", "v": "1" },
                    { "n": "dc.p0", "v": "HD720p" },
                    { "n": "dc.vlose", "v": "0" },
                    { "n": "dc.p1", "v": "D1" },
                    { "n": "dc.model", "v": "f136" },
                    { "n": "dc.loc", "v": "{{CAMERA_LOCATION}}" },
                    { "n": "dc.cputype", "v": "gm8135" },
                    { "n": "dc.wifi", "v": "rtl8188fu" },
                    { "n": "dc.sensortype", "v": "soih62" },
                    { "n": "dc.nick", "v": "{{CAMERA_NICKNAME}}" },
                    { "n": "dc.auto_enter_config", "v": "1" },
                    { "n": "f_log", "v": "1" },
                    { "n": "flog", "v": "all" },
                    { "n": "f_scene", "v": "1" },
                    { "n": "f_rfdev", "v": "1" },
                    { "n": "f_cld", "v": "1" },
                    { "n": "f_web", "v": "1" },
                    { "n": "sc.iot", "v": "1" },
                    { "n": "sc.alexa_link", "v": "enable" },
                    { "n": "sc.netcheck.enable", "v": "1" },
                    { "n": "sc.sndlogver", "v": "v0" },
                    { "n": "f_no_about", "v": "1" },
                    { "n": "sc.vboxstat", "v": "" }
                ]
            }
        ]
    }
}
```

En cas d'erreur la valeur `data.ret.code` ne sera pas vide.

Dans le cas d'une absence d'appareil, `data.devs` ne sera pas présente.

Par la suite, la valeur `data.devs.*.sn` sera désignée par `SN`

### /ccm_pic_get.jpg

Permet de récupérer une capture d'écran de la caméra, une image fixe au moment de la requête.

`http://{{IP}}:{{PORT}}/ccm/ccm_pic_get.js`

Paramètres :

- `dsess` : `1`

- `dsess_nid` : [`NID`](#cacs_login_reqjs)

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `dtoken` : `p1_xxxxxxxxxx` _Utilisation inconnue_

- `dencode_type` : `0` _Utilisation inconnue_

- `dpic_types_support` : `2` _Utilisation inconnue_

- `dflag` : `2` _Utilisation inconnue_

### /ccm_play.js

Permet de récupérer le lien du flux de la caméra.

`http://{{IP}}:{{PORT}}/ccm/ccm_play.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1`

- `dsess_nid` : Générée grâce à la fonction nid du module [mcodec](/mipc%20source%20code/extract/mcodec.js)
  
  ```js
  mcodec.nid(seq, sid, sharedKey, 0, null, null, md5, "hex")
  ```
  
    où : 
  
  - `seq` : valeur actuelle de la variable à incrémenter ([`hfrom_handle`](#paramètres-génériques))
  
  - `lid` : [`LID`](#cacs_dh_reqjs)
  
  - `sharedKey` : [`SHARED_KEY`](#cacs_login_reqjs)

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `dsetup` : `1` _Utilisation inconnue_

- `dsetup_stream` : `RTSP` Définit le type de flux. (À l'origine : `RTP_Unicast`).

- `dsetup_trans` : `1` _Utilisation inconnue_

- `dsetup_trans_proto` : `rtsp` (À l'origine : `http`).

- `dtoken` : `p0` _Utilisation inconnue_

Exemple de réponse (JSON) : 

```json
{
    "type": "GetStreamUriResponse",
    "from": 270532608,
    "from_handle": 275550831,
    "to_handle": 17,
    "data": {
        "Result": { "Code": "", "SubCode": "", "Reason": "", "Desc": "" },
        "MediaUri": {
            "Uri": "rtsp://{{STREAM_IP}}:{{STREAM_PORT}}/live/{{SN}}_p0_{{TOKEN}}",
            "InvalidAfterConnect": 0,
            "InvalidAfterReboot": 0,
            "Timeout": 0
        },
        "media_id": "cms_oveu11_2"
    }
}
```

### /ccm_dev_info_get.js

Permet d'obtenir plus d'informations à propos d'un appareil.

`http://{{IP}}:{{PORT}}/ccm/ccm_dev_info_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) :

```json
{
    "type": "ccm_dev_info_get_ack",
    "from": 270532608,
    "from_handle": 275674876,
    "to_handle": 2872,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "mfc": "",
        "model": "f136",
        "bimg_ver": "v5.1.8.1807231606",
        "img_ver": "v5.3.1.2003161406",
        "sn": "{{CAMERA_ID}}",
        "dev_id": "{{CAMERA_ID}}",
        "nick": "{{CAMERA_NICKNAME}}",
        "type": "IPC",
        "wifi": "rtl8188fu",
        "os": "gm8135_v2",
        "sensor": "soih62",
        "p": [
            { "n": "p2", "v": "CIF" },
            { "n": "s.pwdw", "v": "0" },
            { "n": "s.new", "v": "1" },
            { "n": "timezone_min", "v": "0" },
            { "n": "sncf", "v": "v1v2" },
            { "n": "s.sound_detect", "v": "0" },
            { "n": "nick", "v": "{{CAMERA_NICKNAME}}" },
            { "n": "dc.record_mode", "v": "1" },
            { "n": "s.pic_cloud", "v": "1" },
            { "n": "s.noio", "v": "1" },
            { "n": "bimg_ver", "v": "v5.1.8.1807231606" },
            { "n": "img_ver", "v": "v5.3.1.2003161406" },
            { "n": "dc.new_ealf", "v": "1" },
            { "n": "wfcnr", "v": "2" },
            { "n": "oncnt", "v": "1" },
            { "n": "type", "v": "IPC" },
            { "n": "s.sys_ok_audio", "v": "1" },
            { "n": "dc.board_type", "v": "board.cfg.ptz.gm8135.nostop" },
            { "n": "s.first_config", "v": "1" },
            { "n": "s.sensor", "v": "ok" },
            { "n": "dc.cpu_type", "v": "gm8135" },
            { "n": "s.wifq", "v": "82" },
            { "n": "s.maxid", "v": "0" },
            { "n": "s.minid", "v": "1" },
            { "n": "s.wifs", "v": "srvok" },
            { "n": "s.eifs", "v": "ifaceok" },
            { "n": "t_pwr", "v": "2023-09-13 07:35:24.000+01:00" },
            { "n": "s.cloud", "v": "1" },
            { "n": "s.audio_alarm_manually", "v": "1" },
            { "n": "s.nwwan", "v": "null" },
            { "n": "s.nwlan", "v": "ok" },
            { "n": "sn", "v": "{{CAMERA_ID}}" },
            { "n": "timezone", "v": "2" },
            { "n": "s.motion_track", "v": "0" },
            {
                "n": "mvar",
                "v": { "mvar_boot_times": 1, "bootc_pwr": 1, "bootc_reboot": 1, "t_pwr": 1694590524, "t_reboot": 1694590524, "t_boot": 1694590524 }
            },
            { "n": "t_boot", "v": "2023-09-13 07:35:24.000+01:00" },
            { "n": "pcrc", "v": "4235323954" },
            { "n": "s.cmd", "v": "1" },
            { "n": "s.audio_alarm", "v": "1" },
            { "n": "s.spv", "v": "1" },
            { "n": "s.neth", "v": "ok" },
            { "n": "s.search_by_cid", "v": "1" },
            { "n": "s.motion", "v": "stop" },
            { "n": "model", "v": "f136" },
            { "n": "s.record", "v": "0" },
            { "n": "s.code_match", "v": "1" },
            { "n": "t_reboot", "v": "2023-09-13 07:35:24.000+01:00" },
            { "n": "s.alert", "v": "0" },
            { "n": "s.oscene", "v": "1" },
            { "n": "s.vlose", "v": "0" },
            { "n": "s.qrc", "v": "no" },
            { "n": "feature", "v": "3" },
            { "n": "p0", "v": "HD720p" },
            { "n": "uptime", "v": "8259" },
            { "n": "p1", "v": "D1" },
            { "n": "s.cloud_mul_chn", "v": "1" }
        ]
    }
}
```

### /ccm_ntp_get.js

Fournit des informations sur le réseau auquel la caméra est connectée.

`http://{{IP}}:{{PORT}}/ccm/ccm_ntp_get.js`

Paramètres :

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `dtokens__x_countz_` : `2`

- `dtokens` : `eth0`

- `dtokens_1` : `ra0`

- `ditems__x_countz_` : `2`

- `ditems` : `all`

- `ditems_1` : `all`

- `dforce_scan` : `1`

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_net_get_ack",
    "from": 270532608,
    "from_handle": 275674894,
    "to_handle": 2873,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "info": {
            "ifs": [
                {
                    "token": "eth0",
                    "enabled": 0,
                    "phy": {
                        "conf": { "mode": "ether", "mtu": 1500 },
                        "info": {
                            "name": "eth0",
                            "type": "",
                            "mac": "{{MAC_ADDRESS}}",
                            "stat": "err"
                        }
                    },
                    "ipv4": {
                        "conf": {
                            "enabled": 1,
                            "mode": "dhcp",
                            "static_ip": {
                                "addr": "{{LOCAL_IP}}",
                                "mask": "{{MASK}}",
                                "gw": "0.0.0.0"
                            }
                        },
                        "info": {
                            "stat": "err",
                            "ip": { "addr": "0.0.0.0", "mask": "0.0.0.0", "gw": "0.0.0.0" }
                        }
                    }
                },
                {
                    "token": "ra0",
                    "enabled": 1,
                    "phy": {
                        "conf": { "mode": "wificlient", "mtu": 1500 },
                        "info": {
                            "name": "ra0",
                            "type": "",
                            "mac": "{{MAC_ADDRESS}}",
                            "stat": "ok"
                        }
                    },
                    "ipv4": {
                        "conf": {
                            "enabled": 1,
                            "mode": "static",
                            "static_ip": {
                                "addr": "{{LOCAL_IP_2}}",
                                "mask": "{{MASK}}",
                                "gw": "{{GATEAWAY}}"
                            },
                            "debug_ip": { "addr": "0.0.0.0", "mask": "0.0.0.0", "gw": "0.0.0.0" }
                        },
                        "info": {
                            "stat": "ok",
                            "ip": {
                                "addr": "{{LOCAL_IP_2}}",
                                "mask": "{{MASK}}",
                                "gw": "{{GATEAWAY}}"
                            }
                        }
                    },
                    "wifi_client": {
                        "conf": {
                            "enabled": 1,
                            "ssid": "{{WIFI_SSID}}",
                            "bssid": "",
                            "auth_mod": "",
                            "encrypt_mod": "",
                            "key": "******",
                            "usr": "{{WIFI_USER}}"
                        },
                        "info": { "channel": 3, "stat": "ok" },
                        "ap_list": [
                            {
                                "ssid": "{{WIFI_SSID}}",
                                "connect": 1,
                                "quality": 97,
                                "bss": "{{BSS}}",
                                "proto": "IEEE 802.11bgn",
                                "mode": "Master",
                                "freq": "2.422 GHz Channel(3)",
                                "signal": 100,
                                "noise": 0,
                                "signal_dbm": 0,
                                "noise_dbm": 0,
                                "bitrate": "300 Mb/s",
                                "encrypt": "on",
                                "adhoc": 0
                            }
                        ]
                    },
                    "wifi_adhoc": {
                        "conf": {
                            "enabled": 1,
                            "freq_select": "",
                            "ssid": "IPC{{CAMERA_ID}}",
                            "auth_mod": "OPEN",
                            "encrypt_mod": "NONE",
                            "key": "xxxxxxx",
                            "channel": 0
                        }
                    },
                    "dhcp_srv": {
                        "conf": {
                            "enabled": 1,
                            "gw": "{{LOCAL_IP}}",
                            "mask": "{{MASK}}",
                            "ip_start": "{{LOCAL_IP_START}}",
                            "ip_end": "{{LOCAL_IP_END}}"
                        }
                    }
                }
            ],
            "dns": {
                "conf": { "enabled": 0, "mode": "dhcp", "static_dns": ["{{DNS_1}}"] },
                "info": { "stat": "ok", "dns": ["{{DNS_2}}", "{{DNS_3}}"] }
            }
        }
    }
}
```

### /ccm_date_get.js

Fournit la date et l'heure interne de la caméra.

`http://{{IP}}:{{PORT}}/ccm/ccm_date_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_date_get_ack",
    "from": 270532608,
    "from_handle": 275826134,
    "to_handle": 2974,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "utc_date": {
            "time": { "hour": 12, "min": 20, "sec": 58 },
            "date": { "year": 2023, "mon": 9, "day": 13 }
        }
    }
}
```

### /ccm_disk_get.js

Fournit des informations sur la carte SD.

`http://{{IP}}:{{PORT}}/ccm/ccm_disk_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_disk_get_ack",
    "from": 270532608,
    "from_handle": 275835165,
    "to_handle": 2983,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "disks": [
            {
                "token": "sd",
                "stat": "mount",
                "size": 15104,
                "available_size": 256,
                "used_size": 14848,
                "dk_has_err": 0,
                "sd_compatible_show": 0,
                "sd_compatible_mode": "",
                "conf": {
                    "enable": 1,
                    "low_space": 200,
                    "msg_queue_length": 10000,
                    "low_space_ratio": 0.08,
                    "middle_space_ratio": 0.6,
                    "clear_space": 300,
                    "record_mode": 50,
                    "sd_check_on_line": 1,
                    "sd_alarm": 0,
                    "record_alarm": 0
                }
            }
        ]
    }
}
```

### /mmq_pick.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/mmq_pick.js`

Paramètres :

- `hqid` : [`QID`](#mmq_createjs)

- `dqid` : [`QID`](#mmq_createjs)

- `dtimeout` : `100000` 

Exemple de réponse (JSON) :

```json
{
    "type": "ccm_msg",
    "from": 270532608,
    "to_handle": 2987,
    "data": {
        "sess": { "nid": "{{NID}}", "sn": "{{SN}}" },
        "items": [
            {
                "msg_id": 56,
                "sn": "{{SN}}",
                "user": "",
                "date": 1694600614,
                "type": "play",
                "code": "start",
                "p": [
                    { "n": "min_id", "v": "1" }
                ]
            }
        ]
    }
}
```

### /ccm_subscribe.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_subscribe.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_subscribe_ack",
    "from": 270532608,
    "from_handle": 275752767,
    "to_handle": 2908,
    "data": { "ret": { "code": "", "sub": "", "reason": "", "desc": "" } }
}
```

### /ccm_dev_action_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_dev_action_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `daction_name` : `oflag` _Utilisation inconnue_

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_dev_action_get_ack",
    "from": 270532608,
    "from_handle": 275678500,
    "to_handle": 2881,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "info": {
            "name": "oflag",
            "enable": 0,
            "dev": [
                { "id": "motion", "nick": "motion" },
                { "id": "sound_detect", "nick": "\0ound_detect" },
                { "id": "face_detect", "nick": "ect\0_detect" },
                { "id": "human_detect", "nick": "\0uman_detect" }
            ]
        }
    }
}
```

### /ccm_plan_record_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_plan_record_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_plan_record_get_ack",
    "from": 270532608,
    "from_handle": 275904508,
    "to_handle": 3042,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "sche": {
            "plan": [
                {
                    "start": 0,
                    "end": 604800,
                    "index": 0,
                    "mode": "",
                    "flag": 2,
                    "action_name": [
                        { "name": "record", "times": 0, "control_time": 0, "continue_time": 604800 }
                    ]
                }
            ]
        }
    }
}
```

### /ccm_action_sche_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_action_sche_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` 

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `dexdev_id` : `motion` _Utilisation inconnue_

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_action_sche_get_ack",
    "from": 270532608,
    "from_handle": 275904494,
    "to_handle": 3041,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "sche": {
            "all": 0,
            "dev_name": "motion",
            "plan": [
                {
                    "start": 0,
                    "end": 604800,
                    "index": 0,
                    "mode": "",
                    "flag": 10,
                    "action_name": [
                        {
                            "name": "cloud",
                            "times": 0,
                            "control_time": 8000,
                            "continue_time": 16000
                        },
                        {
                            "name": "record",
                            "times": 0,
                            "control_time": 8000,
                            "continue_time": 16000
                        }
                    ]
                }
            ]
        },
        "alarm_mode": { "mode": 0, "period": 0, "timeout": 0 }
    }
}
```

### /ccm_dev_profile_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_dev_profile_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_dev_profile_get_ack",
    "from": 270532608,
    "from_handle": 275904484,
    "to_handle": 3040,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "info": {
            "dev": [
                { "enable": 1, "id": "motion", "nick": "motion", "type": 1 },
                { "enable": 1, "id": "sound_detect", "nick": "sound_detect", "type": 9 },
                { "enable": 1, "id": "face_detect", "nick": "face_detect", "type": 8 },
                { "enable": 1, "id": "human_detect", "nick": "human_detect", "type": 10 }
            ]
        }
    }
}
```

### /ccm_box_conf_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_box_conf_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_box_conf_get_ack",
    "from": 270532608,
    "from_handle": 275903932,
    "to_handle": 3038,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "conf": [
            {
                "enable": 0,
                "username": "",
                "password": "",
                "is_ps2": 0,
                "code_match": 0,
                "sn": "",
                "nick": "",
                "uuid": "",
                "type": ""
            }
        ],
        "connect": 0
    }
}
```

### /ccm_upgrade_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_upgrade_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `dcheck` : `1`

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_upgrade_get_ack",
    "from": 270532608,
    "from_handle": 275923581,
    "to_handle": 3064,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "stat": "",
        "progress": 0,
        "_cur_ver": "v5.3.1.2003161406",
        "_valid_ver": "v5.3.1.2003161406",
        "remark": "",
        "os_ver": "gm8135_v2",
        "img_ver": "v5.1.8.1807231606",
        "prj_ver": "v5.3.1.2003161406",
        "valid_ver": ["v5.3.1.2003161406"],
        "hw_ext": "rtl8188fu",
        "img_ext": "rtl8188fu",
        "prj_ext": "rtl8188fu",
        "baseline_upgrade": 0,
        "upgrade_time": 0
    }
}
```

### /ccm_speaker_get.js

Fournit des informations sur le haut-parleur de la caméra.

`http://{{IP}}:{{PORT}}/ccm/ccm_speaker_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `dtoken` : `ao0`

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_speaker_get_ack",
    "from": 270532608,
    "from_handle": 275920818,
    "to_handle": 3057,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "conf": { "token": "ao0", "level": 50, "alarm_level": "100" }
    }
}
```

### /ccm_video_srcs_get.js

Fournit des informations sur la video.

`http://{{IP}}:{{PORT}}/ccm/ccm_video_srcs_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_video_srcs_get_ack",
    "from": 270532608,
    "from_handle": 275920820,
    "to_handle": 3058,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "vss": [
            {
                "token": "vs0",
                "framerate": 25,
                "resolution": { "width": 704, "height": 576 },
                "extension": {
                    "conf": {
                        "mode": "auto",
                        "light_mode": "",
                        "day_or_night": 0,
                        "red_or_white": 0,
                        "brightness": 83,
                        "color_saturation": 70,
                        "contrast": 86,
                        "sharpness": 44
                    }
                }
            }
        ]
    }
}
```

### /ccm_mic_get.js

Fournit des informations sur le microphone.

`http://{{IP}}:{{PORT}}/ccm/ccm_mic_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_mic_get_ack",
    "from": 270532608,
    "from_handle": 275920824,
    "to_handle": 3059,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "conf": [
            {
                "entity": { "name": "asc3", "use_counts": 0, "token": "asc3" },
                "token": "dev3",
                "level": 100,
                "silent": 0
            }
        ]
    }
}
```

### /ccm_misc_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_misc_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_misc_get_ack",
    "from": 270532608,
    "from_handle": 275920828,
    "to_handle": 3060,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "info": { "flip": 0, "power_freq": 1 },
        "resolute": "16:9"
    }
}
```

### /ccm_osd_get.js

_Utilisation inconnue_

`http://{{IP}}:{{PORT}}/ccm/ccm_osd_get.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` _Utilisation inconnue_

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_osd_get_ack",
    "from": 270532608,
    "from_handle": 275835103,
    "to_handle": 2982,
    "data": {
        "ret": { "code": "", "sub": "", "reason": "", "desc": "" },
        "osd": {
            "text": "",
            "text_enable": 0,
            "logo_disable": 0,
            "date": { "format": "YYYY-MM-DD", "enable_12h": 0, "date_enable": 1, "time_enable": 1 },
            "week": 1
        }
    }
}
```

### /ccm_speaker_set.js

Definit les paramètres du haut-parleur.

`http://{{IP}}:{{PORT}}/ccm/ccm_speaker_set.js`

Paramètres : 

- `hqid` : [`QID`](#mmq_createjs)

- `dsess` : `1` 

- `dsess_nid` : `NID`

- `dsess_sn` : [`SN`](#ccm_devs_getjs)

- `dconf` : `1` _Utilisation inconnue_

- `dconf_token` : `ao0` _Utilisation inconnue_

- `dconf_level` : `75` Le niveau du haut-parleur sur 100.

- `dforce_persistence` : `1` _Utilisation inconnue_

Exemple de réponse (JSON) : 

```json
{
    "type": "ccm_speaker_set_ack",
    "from": 270532608,
    "from_handle": 275984055,
    "to_handle": 3112,
    "data": { "ret": { "code": "", "sub": "", "reason": "", "desc": "" } }
}
```

### /ccm_ptz_ctl.js

Permet de contrôler les mouvements de la caméra.

`http://{{IP}}:{{PORT}}/ccm/ccm_ptz_ctl.js`
