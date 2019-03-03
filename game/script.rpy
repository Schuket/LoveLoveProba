#Usefull Keyword

#GUI

#define gui.textbox_height = 220

#Animation


# Transition
define flash = Fade(.25, 0.0, .75, color="#fff")
define sleep = Fade(0.5, 2.0, 0.5)

#Background
image bg room = "background/room.png"
image bg park = "background/park.png"
image bg street = "background/rue.png"
image bg end = "background/credits_screen.png"

image device = "other/device.png"
image device bug animated:
    "other/device.png"
    pause 0.1
    "other/device_bug.png"
    pause 0.1
    repeat

#Collectible

image cg alien good = "cg/CG_Alien_Good.png"
image cg alien bad = "cg/CG_Alien_Bad.png"

image cg monster good = "cg/CG_Monstre_Good.png"
image cg monster bad = "cg/CG_Monstre_Bad.png"

#Image Character
# Human
image human = "character/humain_neutre.png"
image human shadow = "character/humain_ombre.png"
image human smile = "character/humain_joie.png"
image human angry = "character/humain_colere.png"

# Alien
image alien = "character/alien_neutre.png"
image alien shadow = "character/alien_ombre.png"
image alien smile = "character/alien_joie.png"
image alien angry = "character/alien_colere.png"

# Monster
image monster = "character/monstre_neutre.png"
image monster shadow = "character/monstre_ombre.png"
image monster smile = "character/monstre_joie.png"
image monster wink = "character/monstre_wink.png"

#Character
define Narrator = Character(what_italic=True)
define Player = Character("[playername]", color="#ff69b4")

define Computer = Character("[playername]", who_font="font/notalot35.ttf", who_size=50, what_font="font/notalot35.ttf", what_size= 35)
define ComputerUnknown = Character("???", color="#d3d3d3", who_font="font/notalot35.ttf", who_size=50, what_font="font/notalot35.ttf", what_size= 35)
define ComputerAlien = Character("SweetBeauty", who_font="font/notalot35.ttf", who_size=50, what_font="font/notalot35.ttf", what_size= 35)

define Unknown = Character("???", color="#d3d3d3")
define Human = Character("Rachel", color="#4c4cff")

define Alien = Character("SweetBeauty", color="#009900")
define AlienCamille = Character("Camille", color="#009900")

define Monster = Character("Cthulhu", color="#bf5fff")

# Variable

define human_love = 50
define alien_love = 50
define monster_love = 50

# Usefull func

label device_appear:

    show device:
        xalign 0.5
        yalign 0.0
    with dissolve

    return


#label main_menu:

label start:

    #sound
    stop music fadeout 2.0

    #background
    scene bg room

    # Get Player Name
    $ playername = renpy.input("Quel est ton nom, jeune galopin ?", "Dr. Love")
    $ playername = playername.strip()

    if not playername:
        $ playername = "Dr. Love"

    play sound "sound/modem.mp3"
    pause 7.0
    play music "sound/main_loop.ogg" fadein 3.0 loop
    play sound "sound/clavier.mp3" loop

    # Begin VN
    jump main

label main:

    #play modem sound

    #Intro
    Narrator "{alpha=-0.3}Pfiou… Enfin cette looongue journée de travail au labo est terminée ! Je vais pouvoir me remettre enfin à mes recherches sur la drague...{/alpha}"
    Narrator "{alpha=-0.3}Aussi étrange que cela puisse paraître, la probabilité de succès des phrases pré-faites sur le net semble plutôt grande. J’ai hâte de mettre en action ce que j’ai appris dernièrement.{/alpha}"
    Narrator "{alpha=-0.3}Cela fait bientôt plus d’un mois que je travaille dessus, probabilité sur probabilité de ce qui fonctionnera le plus dans différents types de rencontre. {/alpha}"
    Narrator "{alpha=-0.3}J’ai même conçu mon propre Lovo’mètre, qui me donne en temps réel les pourcentages de réussite d’une phrase de drague pré-faite. {/alpha}"

    call Tuto

    Player "{alpha=-0.3}Tout à l'air en ordre.{/alpha}"
    Narrator "{alpha=-0.3}J’ouvre ma page favorite, “les 100 meilleures phrases pour pécho à coup sûr”. Je l’ai découverte il y a peu et j’essaie d’apprendre chaque phrase par coeur…{/alpha}"
    Narrator "{alpha=-0.3}C’est fou comme jouer un rôle permet d’atteindre ses objectifs. Être soi-même devient tellement inutile.{/alpha}"
    Narrator "{alpha=-0.3}Je me rappelle avoir posté un message sur le nouveau forum “Meet me tomorrow”, voyons si quelqu’un m’a répondu.{/alpha}"

    #Computer Conv' with Alien Beauty
    Player "Non?! J’ai bien eu une réponse !"
    Narrator "{alpha=-0.3}Je lis et relis le message avec émoi.{/alpha}"
    ComputerUnknown "Bonjour [playername], ton message m’a beaucoup plu et je pense que nous avons beaucoup de choses à partager!"
    ComputerUnknown "Je te propose donc un rendez-vous au Love Love Parc en début d’après midi demain. 15h te conviendrait-il ?"
    ComputerUnknown "J’attends avec hâte ta réponse!\nBien à toi,\nSweet Beauty"
    Narrator "{alpha=-0.3}Je réponds dans la précipitation ayant trop peur de rater l’opportunité.{/alpha}"
    Computer "J’accepte avec plaisir ! Comment pourrais-je te reconnaître?"
    ComputerAlien "Super ! Je porterais des lunettes noires. Et j’ai les cheveux bruns mi-longs et bouclés."
    ComputerAlien "Tu verras, je sors de l’ordinaire, tu me reconnaîtra tout de suite !\nA très vite,\nSweet Beauty"
    Narrator "{alpha=-0.3}Je n’en revenais pas ! Après tout ce temps à chercher, j’ai enfin réussi à avoir un rendez-vous ! C’est pas le moment de se louper. Je me remet sur ma page internet d’astuces, et récite à voix haute plusieurs fois cette longue liste d’une centaine de phrases. {/alpha}"
    stop sound fadeout 2.0
    Narrator "{alpha=-0.3}Le temps passe vraiment vite il est déjà 3h du matin, je me dépêche de rejoindre mon lit !{/alpha}"

    jump Act_1

##### TUTO #################################################################################################################

label Tuto:

    Player "Profitons-en pour régler les paramètres !"

    call device_appear
    menu:

        Player "Voyons-voir si ça fonctionne correctement ..."

        "{color=#00ff00}100 \%{/color}\nRéussite Total !":
            hide device
            with dissolve
            jump Tuto_Good

        "{color=#ffff00}50 \%{/color}\nÇa passe ou ça casse !":
            hide device
            with dissolve
            jump Tuto_Average

        "{color=#ff0000}0 \%{/color}\nÇa ne fonctionnera pas ...":
            hide device
            with dissolve
            jump Tuto_Bad

label Tuto_Good:

    Narrator "{alpha=-0.3}C'est super efficace ! C'est avec ce genre de réplique que j'arriverais à mes fins !{/alpha}"
    return

label Tuto_Average:

    Narrator "{alpha=-0.3}Un résultat mitigé... En fonction du temps et de l'alignement des astres je présume... {/alpha}"
    return

label Tuto_Bad:

    Narrator "{alpha=-0.3}Échec critique ! À éviter si vous tenez à la personne d'en face {cps= 3}... Ou à la vie ...{/cps} {/alpha}"
    return


##### ACTE 1 #################################################################################################################

label Act_1:


    scene bg room
    with sleep

    #Already Late !
    Narrator "{alpha=-0.3}J’ouvre un oeil, je me sens reposé. Je regarde l’heure, je ne capte pas tout de suite... Il est 15h30.{/alpha}"
    Player "{size=+40} QUOIII??!!? {/size}"
    Player "Mais mon réveil? {cps= 3}Oh…{/cps} J’ai complètement oublié de le mettre !"
    Narrator "{alpha=-0.3}Je me prépare rapidement et prends mon Lovo’mètre avec moi.{/alpha}"
    play sound "sound/footsteps2.mp3"

    scene bg street
    with fade
    play sound "sound/ambiance_street.ogg" fadein 3.0 loop

    #Encounter with a Girl
    Narrator "{alpha=-0.3}Je suis en train de courir en direction du parc quand tout à coup{cps= 3}…{/cps} Je heurte de plein fouet une personne.{/alpha}"
    Narrator "{alpha=-0.3}Elle se retourne vers moi outrée.{/alpha}"

    show human shadow
    with vpunch and hpunch
    show human
    with flash

    Unknown "{size= +20}Eh mais vous pourriez faire attention !{/size}"
    Narrator "{alpha=-0.3}{cps= +30}Mayday !{/cps} Mon Lovo’mètre devrait m’aider{/alpha}"

    call device_appear
    menu:

        Narrator "{alpha=-0.3}{cps= 10}J’hésite…{/cps} Elle est plutôt mignonne dans son genre. Mais je suis vraiment en retard pour mon rendez-vous.{/alpha}"

        "{color=#00ff00}100 \%{/color}\nDécider de rester et\n entamer une conversation\n avec cette jeune femme":
            hide device
            with dissolve
            jump Act_1_ask_1_answer_1


        "{color=#ff0000}0 \%{/color}\nL’ignorer complètement\n et reprendre la route\n vers le parc":
            hide device
            with dissolve
            jump Act_1_ask_1_answer_2


label Act_1_ask_1_answer_1:

    Narrator "{alpha=-0.3}Je regarde la jeune inconnue et lui sors mon plus beau sourire. De toute façon c’est toujours bon de se faire désirer.{/alpha}"
    jump Act_1_ask_2

label Act_1_ask_1_answer_2:

    Narrator "{alpha=-0.3}La jeune inconnue m’attrape par le bras.{/alpha}"
    Unknown "Et en plus vous fuyez? Mais vous êtes vraiment un {size=+5}goujat{/size} ! La moindre des choses serait de s’excuser pour commencer !"
    Narrator "{alpha=-0.3}C’est loupé pour mon rencard. Mais bon se faire désirer est une bonne chose{cps=10}, non?{/cps}{/alpha}"
    jump Act_1_ask_2


label Act_1_ask_2: # Question 2

    call device_appear
    menu:

        "{color=#00ff00}60 \%{/color}\n…Tu es tellement belle\nque j’en ai oublié\nma phrase d’accroche…":
            hide device
            with dissolve
            show human smile
            with dissolve
            $ human_love += 15
            jump Act_1_ask_2_answer_1 # +

        "{color=#ff0000}10 \%{/color}\nEtait-ce un\n tremblement de terre\n ou as-tu simplement\n ébranlé mon monde ?":
            hide device
            with dissolve
            show human angry
            with dissolve
            $ human_love -= 20
            jump Act_1_ask_2_answer_2 # -

        "{color=#ffff00}30 \%{/color}\nP-p-pardon…\n Qu-qu-quel est ton prénom ?":
            hide device
            with dissolve
            jump Act_1_ask_2_answer_3 # ~


label Act_1_ask_2_answer_1:

    Narrator "{alpha=-0.3}Mmh celle là j’en suis plutôt fier !{/alpha}"
    Unknown "Oh… Je t’intimide à ce point? C’est mignon. Original pour une fois. Evite quand même de bousculer les gens sur ton passage la prochaine fois."

    jump Act_1_ask_3

label Act_1_ask_2_answer_2:

    Unknown "Sérieusement? T’as rien trouvé de mieux? Je dirais plutôt que tu m’a bousculée, rien à voir avec un tremblement de terre, et ce genre de catastrophe n’arrive pas par ici. Renseigne toi un peu avant d’ouvrir la bouche."
    jump Act_1_ask_3


label Act_1_ask_2_answer_3:

    Unknown "Eh merde… Encore un bègue. Prends ton temps pour parler, t’inquiètes pas je ne juge pas. Fais quand même attention, regarde où tu vas la prochaine fois au lieu de regarder tes pieds."
    jump Act_1_ask_3


label Act_1_ask_3: # Question 3

    show human
    with dissolve
    Human "Au fait, moi c’est Rachel, Mr. \"je suis très pressé\". Je me présente car je sais être polie. Tu connais ce mot? En définition ça veut dire qu’on évite de bousculer les gens dans la rue sans un minimum d’excuse. Ca s’appelle aussi le savoir vivre."

    call device_appear
    menu:

        "{color=#ff0000}10 \%{/color}\nEmbrasse moi si j’ai tord,\n on s’est déjà rencontré non ?":
            hide device
            with dissolve
            show human angry
            with dissolve
            $ human_love -= 20
            jump Act_1_ask_3_answer_1 # -

        "{color=#00ff00}60 \%{/color}\nEst-ce que tu as un pansement ?\n Je viens de m’écorcher\nle genou en tombant sur toi":
            hide device
            with dissolve
            show human smile
            with dissolve
            $ human_love += 15
            jump Act_1_ask_3_answer_2 # +

        "{color=#ffff00}30 \%{/color}\nEs-tu magicienne ?\n Parce que quand\n je te regarde\n tout le reste disparaît...":
            hide device
            with dissolve
            jump Act_1_ask_3_answer_3 # ~


label Act_1_ask_3_answer_1:

    Human "Waw, j’suis vraiment tentée de te répondre que oui on s’est déjà rencontré. Tu veux savoir où? Oh désolée mais tu es tellement insignifiant et inintéressant que j’ai vraiment du mal à m’en rappeler clairement"
    jump Act_1_ask_4

label Act_1_ask_3_answer_2:

    Human "Quoi? Oh oui bien sûr je dois avoir ça quelque part"
    Narrator "{alpha=-0.3}Elle cherche un pansement dans son sac à main, j’en profite pour bien la reluquer de haut en bas. Elle soupire et se tourne à nouveau vers moi.{/alpha}"
    Human "Et nan… Désolée mec. Tu vas devoir apprendre à survivre malgré cette blessure vraiment grave !" # oui ou non ? *rires*
    Narrator "{alpha=-0.3}Elle rigole. C’est bon signe ça non ?{/alpha}"
    jump Act_1_ask_4

label Act_1_ask_3_answer_3:

    Human "J’aimerais vraiment savoir faire disparaitre les choses, surtout une en particulier à ce moment précis. Mais non, malheureusement je n’ai pas ce pouvoir, sinon je ne te verrais déjà plus."
    jump Act_1_ask_4

label Act_1_ask_4:

    show human
    with dissolve
    Human "Bref, j’attends quand même toujours mes excuses Mr Beau Parleur. Me prendre des gens dans la tronche c’est pas vraiment mon truc."
    Human "Regarde, c’est pas très difficile. Tu mets des mots gentils les un après les autres, en commençant par “Je suis désolé…”. J’pense que tout le monde en est capable, même les plus attardés.”"

    call device_appear
    menu:

        "{size=-0}{color=#ffff00}30 \%{/color}\nOuais j'suis désolé.\n Et pour me faire pardonner\n je vais te faire un cadeau, voici\n les clés de mon appart, de ma voiture\n et je n’oublierais pas…\n celles de mon coeur.{/size}":
            hide device
            with dissolve
            jump Act_1_ask_4_answer_1 # ~

        "{size=-0}{color=#ff0000}10 \%{/color}\nOh excuse moi,\n c’est vrai que tu dois être essoufflée\n à force de courir dans mes rêves.\n Je te laisse reprendre\n ta respiration, la suite va te plaire !{/size}":
            hide device
            with dissolve
            show human angry
            with dissolve
            $ human_love -= 20
            jump Act_1_ask_4_answer_2 # -

        "{size=-0}{color=#00ff00}60 \%{/color}\nJe suis vraiment désolé…\n Mais si jamais je devais te demander\n de sortir pour un rendez-vous,\n ta réponse serait la même\n que la réponse à cette question{/size}":
            hide device
            with dissolve
            show human smile
            with dissolve
            $ human_love += 15
            jump Act_1_ask_4_answer_3 # +

label Act_1_ask_4_answer_1:

    Human "Allez ! Allez ! Je crois que tu en as assez fait. Bel essai vraiment. On peut pas dire que tu n’es pas motivé. Au moins tu t’es excusé c’est le principal. Reprends tes clés va! J’en ai pas besoin. T’as l’air pressé et j’ai des trucs à faire de toute façon."
    jump Act_1_End

label Act_1_ask_4_answer_2:

    Human "En tout cas toi tu prends vraiment tes rêves pour des réalités. Tu vois le mec là bas? C’est mon mec donc me cours pas après si tu tiens à tes genoux."
    Human " La suite ? Mais quelle suite ? J’attendais des excuses, j’en ai à moitié. Tu m’as assez fait perdre mon temps. Dégage de mon chemin"
    jump Act_1_End

label Act_1_ask_4_answer_3:

    Narrator "{alpha=-0.3}Elle rit{/alpha}"
    Human "Haha. On peut dire que tu l’as pas loupée celle là. Elle demande quand même un peu de jugeote, t’es peut être moins bête que tu en as l’air."
    Human "Laisse moi y réfléchir avant de te répondre ! Ouais pourquoi pas, essaie pour voir. Bref ceci dit je dois y aller. On se recroisera sûrement un de ces jours !"
    jump Act_1_End

label Act_1_End:

    show human
    with dissolve
    Human "Allez salut !"
    Narrator "{alpha=-0.3}Et elle s’en va. C’est vrai qu’elle est quand même bien roulée la petite.{/alpha}"
    Narrator "{alpha=-0.3}Zut, j’ai toujours rendez-vous. Je continue mon chemin rapidement en évitant de percuter quelqu’un d’autre.{/alpha}"
    play sound "sound/footsteps2.mp3"

    jump Act_2_ask_1


##### ACTE 2 #################################################################################################################

label Act_2_ask_1:

    scene bg park
    with fade
    play sound "sound/ambiance_park.ogg" fadein 3.0 loop

    Narrator "{alpha=-0.3}Je rentre finalement dans le parc, essayant d’avoir une attitude décontractée.{/alpha}"

    show alien shadow
    with dissolve

    Narrator "{alpha=-0.3}Je remarque une silhouette avec des cheveux bruns mi-longs bouclés. Je m’approche de cette personne espérant que ce soit Sweet Beauty."
    Player "Sweet Beauty?"
    Unknown "Oui c’est bien moi ! Tu dois être [playername]"

    call device_appear
    menu:

        Player "Oui, Je suis vraiment désolé…"

        "{color=#00ff00}60 \%{/color}\nMa grand mère a décidé\n de manger mon Chien.\n C’était un vrai carnage...\n J’ai encore du mal à m’en remettre...":
            hide device
            with dissolve
            show alien
            with dissolve
            jump Act_2_ask_1_answer_1

        "{color=#ff0000}10 \%{/color}\nLe chat de ma voisine\n était coincé dans un arbre.\n Les pompiers n’arrivaient pas,\n je me devais d’intervenir !":
            hide device
            with dissolve
            show alien
            with dissolve
            jump Act_2_ask_1_answer_2

        "{color=#ffff00}30 \%{/color}\nJ’essayais de préparer\n notre mariage !":
            hide device
            with dissolve
            show alien
            with dissolve
            jump Act_2_ask_1_answer_3


label Act_2_ask_1_answer_1:

    Alien "Oh ce dû être affreux ! Je suis vraiment peiné pour votre chien. Avez-vous pensé à faire des funérailles digne de ce nom?"
    Alien "Je peux comprendre votre chagrin, j’ai moi même eu un rocher de compagnie qui s’est brisé en deux suite à un accident… Il se nommait Pierre et je ne m’en suis toujours pas remis. Ne pouvant pas m’en séparer j’ai décidé de l’empailler pour le garder pour toujours auprès de moi"
    jump Act_2_ask_2

label Act_2_ask_1_answer_2:

    Alien "Vous êtes vraiment un héros, je pense ne pas m’être trompé sur votre compte. Je suis en joie de vous rencontrer en ce lieu si grandiose. Vous êtes tout excusé pour votre retard."
    Alien "C’est vraiment très gentil d’aider une vieille dame à chasser son dîner. Les chats sont vraiment succulents. Cette dame devait mourir de faim pour demander de l’aide aux sapeurs pompiers. Vous avez fait une très belle action !"
    jump Act_2_ask_2

label Act_2_ask_1_answer_3:

    Alien "Vous êtes très divertissant ! Un mariage, mais quelle drôle d’idée. Nous venons tout juste de nous rencontrer. Créer lien entre deux personnes jusqu’à la fin de leur vie n’est pas forcément ma tasse de thé."
    jump Act_2_ask_2

label Act_2_ask_2:


    AlienCamille "Je me baptise Camille. Allons, baladons-nous dans cet endroit mirifique. Rien que vous et moi, nous n’aurons plus qu’à faire connaissance, que je puisse me faire une idée sur votre moi intérieur. Vous savez je suis très rougissant comme personne."

    show device bug animated:
        xalign 0.5
        yalign 0.0
    with vpunch

    Narrator "{alpha=-0.3}Hein?!\nBizarre...{/alpha}"

    call device_appear
    menu:

        "{color=#00ff00}60 \%{/color}\nTu me fais penser\n à un appareil photo,\n à chaque fois que je te vois\n je souris.":
            hide device
            with dissolve
            show alien angry
            with dissolve
            jump Act_2_ask_2_answer_1 # -

        "{color=#00ff00}10 \%{/color}\nPas étonnant que\n le ciel soit gris aujourd’hui,\n tout le bleu est dans tes yeux.":
            hide device
            with dissolve
            show alien smile
            with dissolve
            jump Act_2_ask_2_answer_2 # +

        "{color=#00ff00}30 \%{/color}\nIl y a tellement de soleil\n dans tes yeux\n que je bronze quand tu me regarde.":
            hide device
            with dissolve
            jump Act_2_ask_2_answer_3 # ~

label Act_2_ask_2_answer_1:

    AlienCamille "Hum… Me comparer à un objet n’est peut-être pas ce à quoi je m’attendais au premier abord. Est-ce un compliment que vous avez tenté de me faire? Si c’est le cas je pense que c’était assez maladroit de votre part."
    jump Act_2_ask_3

label Act_2_ask_2_answer_2:

    AlienCamille "Oh malgré mes mirifiques lunettes vous avez observé la couleur de mes yeux? Je suis vraiment attendri par vos compliments. Vos yeux quand à eux me laisse sans voix. Je me perds dans le vide galactique qu’ils reflètent. Je me sens à l’aise avec vous"
    jump Act_2_ask_3

label Act_2_ask_2_answer_3:

    AlienCamille "Si je vous fait changer de couleur cela ne me déplaît pas. Evitez tout de même d’être ébloui par ma présence. Je préfèrerais être considéré comme votre égal… Nous ne jouons peut être pas dans la même catégorie mais je peux peut-être faire un effort."
    jump Act_2_ask_3

label Act_2_ask_3:

    show alien
    with dissolve
    AlienCamille "Enfin… Je ne regrette pas d’avoir choisi cet endroit. En plus de la belle vue, il y a pleins de choses à faire pour s’occuper. Avez-vous une idée en tête?"

    call device_appear
    menu:
        "{color=#ffff00}69.333 \%{/color}\nEst-ce que tu peux m’aider?\n Ton corps est composé de 65\% d’eau\n et j’ai très très soif.":
            hide device
            with dissolve
            jump Act_2_ask_3_answer_1 # ~

        "{color=#00ff00}111 \%{/color}\nPuis-je t’offrir un verre\n ou\n veux-tu simplement l’argent?":
            hide device
            with dissolve
            show alien angry
            with dissolve
            $ alien_love -= 20
            jump Act_2_ask_3_answer_2 # -

        "{color=#ff0000}01.0101 \%{/color}\nVeux-tu prendre mon bras,\n que je puisse dire\n à mes amis\n que j’ai été touché par un ange?":
            hide device
            with dissolve
            show alien smile
            with dissolve
            $ alien_love += 15
            jump Act_2_ask_3_answer_3 # +

label Act_2_ask_3_answer_1:

    AlienCamille "Hum… Vous souhaitez boire l’eau de mon corps? Je pense que je vais plutôt vous offrir quelque chose à boire. Les hommes sont vraiment étranges. Je n’imaginais pas une seule seconde qu’ils puissent se boire entre eux."
    AlienCamille "Mais c’est peut-être naturel chez vous. Je préfère m’abstenir pour cet échange. Un verre d’eau ou d’alcool?"
    Player "Pas besoin d’alcool, je suis déjà enivré par votre odeur."
    AlienCamille "Oh… En plus de vous boire entre vous, vous vous reniflez également pour ressentir quelque chose. Vraiment très étrange…"
    jump Act_2_ask_4

label Act_2_ask_3_answer_2:

    AlienCamille "Mais pour qui me prenez vous? Une péripatéticienne? Sachez jeune insolent que jamais je ne m’abaisserais à ce niveau. Ni pour vous ni pour personne ! Vous devriez faire une mise à jour de votre éducation."
    AlienCamille "Ce n’est pas ainsi que vous amènerais un homme à tomber dans vos bras. Je suis beaucoup plus distingué que ça. Veuillez me traiter avec respect."
    jump Act_2_ask_4

label Act_2_ask_3_answer_3:

    AlienCamille "Oh volontier mon cher ami. Vous savez techniquement je suis effectivement en provenance du ciel, je n’aurais jamais pensé que vous l’auriez remarqué. Je suis tout de même l’exemple type du canon de beauté de vo.. de notre espèce. Merci du compliment."
    jump Act_2_ask_4

label Act_2_ask_4:

    show alien
    with dissolve
    AlienCamille "Vous êtes divergent de l’image que je m’étais faite de vous. Un brin innovateur. J’aimerais beaucoup en apprendre plus sur vous."
    AlienCamille "Votre façon de parler me semble très éloignée de ce que je connais. Peut-être pourriez vous m’illuminer sur des sujets que je ne considère pas?"

    call device_appear
    menu:

        Narrator "{alpha=-0.3}On s’asseoit sur un banc en face de l’étang.{/alpha}"

        "{color=#00ff00}@!#$\% \%{/color}\nEst-ce que je peux\n avoir ta photo?\n C’est pour montrer au Père Noël\n ce que je veux comme cadeau.":
            hide device
            with dissolve
            jump Act_2_ask_4_answer_1 # ~

        "{color=#ff0000}@!?#? \%{/color}\nTon cul est tellement beau\n que c’est une honte\n que tu doive t’asseoir dessus.":
            hide device
            with dissolve
            show alien angry
            with dissolve
            $ alien_love -= 20
            jump Act_2_ask_4_answer_2 # -

        "{color=#00ff00}\%!&?/£ \%{/color}\nIl y a des gens qui disent que\n Disneyland est l’endroit le plus\n heureux sur Terre,\n apparemment aucun d’entre eux\n n’a jamais été dans tes bras.":
            hide device
            with dissolve
            show alien smile
            with dissolve
            $ alien_love += 15
            jump Act_2_ask_4_answer_3 # +

label Act_2_ask_4_answer_1:

    AlienCamille "Le Père Noël? Je ne connais pas. C’est le maire de cette ville? Oh… Excusez-moi pour mon ignorance, c’est sûrement le prêtre de votre Église. Je ne savais pas que vous étiez croyant. Je vais peut-être m’y mettre si on vous offre des cadeaux selon vos désirs."
    AlienCamille "En attendant je suis désolée mais je n’aime pas trop les flashs des appareils photos, ils font ressortir mon côté… Peu ordinaire"
    jump Act_2_End

label Act_2_ask_4_answer_2:

    AlienCamille "Comment osez-vous? N’insultez pas mon postérieur ! Certes il est magnifique, je fais beaucoup d’effort pour qu’il soit bien rebondit. Mais la seule motivation que j’ai c’est justement pour le confort de pouvoir m’asseoir dessus."
    AlienCamille "JE ne me permettrais pas de juger vos capacités physiques qui par ailleurs sont plutôt déplorables."
    jump Act_2_End

label Act_2_ask_4_answer_3:

    AlienCamille "Il est vrai que je ne suis jamais allé dans ce parc, comment vous l’appelez déjà? Oui… Disney... Land. J’en ai tout de même vaguement entendu parler."
    AlienCamille " Et si vous comparez ce bonheur à celui d’être en ma présence… Eh bien j’accepte ce compliment avec grand plaisir. Vous êtes vraiment quelqu’un de remarquable. Cet après-midi est vraiment enchanteur."
    jump Act_2_End

label Act_2_End:

    show alien
    with dissolve
    AlienCamille "Il commence à se faire tard. Cette rencontre a été très… Comment dire? Constructive. Je pense avoir beaucoup appris sur vous et vos “méthodes” d’approche avec les inconnus. Je vous souhaite une très bonne soirée."

    if alien_love >= 50:
        call Act_2_Good_End
    else:
        call Act_2_Bad_End

    Narrator "{alpha=-0.3}Etrange ... j'imagine qu'il ne me reste qu'à rentrer.{/alpha}"
    play sound "sound/footsteps2.mp3"
    jump Act_3_ask_1

label Act_2_Good_End:

    scene cg alien good
    with fade
    play sound "sound/chimes.mp3"
    AlienCamille " On se reverra ... sur Terre ou bien ailleurs ... "

    scene bg park
    with fade

    return

label Act_2_Bad_End:

    scene cg alien bad
    with fade
    AlienCamille "J'ai failli oublier {cps=5}... *ZAP* ...{/cps} Désolé, mais je ne peux laisser un être aussi peu subtile se souvenir de moi ... "

    scene bg park
    with fade

    return

##### ACTE 3 #################################################################################################################

label Act_3_ask_1:

    show bg room
    with fade

    Narrator "{alpha=-0.3}Après cette entrevue très instructive, je suis enfin de retour chez moi. Mes avancées sur mes recherches ont dépassé les attentes que j’avais.{/alpha}"
    Narrator "{alpha=-0.3}Je me dépêche de noter tout ça quand je me rend soudain compte que je ne suis pas tout seul dans ma chambre. La silhouette se rapproche de moi.{/alpha}"

    show monster shadow
    with pixellate
    Unknown "Salut! J’ai cru comprendre que tu étais l’As de la drague. On va voir qui l’est vraiment."
    Unknown "Ça ne prendra pas longtemps je te promets, je suis plutôt rapide en besogne. J’aime être efficace et direct. Je ne perds pas mon temps. Je vais à l’essentiel."
    Unknown "Cthulhu va t’apprendre ce que c’est, la vrai drague."

    Narrator "{alpha=-0.3}Je sors mon Lovo’mètre, paniquant un peu. Je ne m’attendais pas à ce qu’on vienne me faire du gringue.{/alpha}"
    Narrator "{alpha=-0.3}Qu’est-ce qui se passe? Les probabilités sont étranges...{/alpha}"

    call device_appear
    menu:

        "{color=#ff78bb}69 \%{/color}\nTu crois à l’amour\n au premier regard ou\n je dois repasser encore une fois?":
            hide device
            with dissolve
            show monster
            with dissolve
            jump Act_3_ask_1_answer_1 # ~

        "{color=#ff78bb}69 \%{/color}\nHum bien sûr.\n Tu n’es peut-être pas\n le plus beau mais..\n J’éteindrais la lumière.":
            hide device
            with dissolve
            show monster wink
            with dissolve
            $ monster_love += 15
            jump Act_3_ask_1_answer_2 # +

        "{color=#ff78bb}69 \%{/color}\nJe ne suis pas un génie\n mais je peux faire que\n tous tes voeux se réalisent.":
            hide device
            with dissolve
            show monster smile
            with dissolve
            $ monster_love -= 20
            jump Act_3_ask_1_answer_3 # -


label Act_3_ask_1_answer_1:

    Monster "Bien sûr que je crois à l’amour au premier regard. Ça s’appelle un coup de foudre. Et malgré le beau temps aujourd’hui, un orage est sur le point d’éclater."
    Monster "Tu risque toi aussi de le prendre de plein fouet. Nos coeurs vibreront ainsi à l’unisson."
    jump Act_3_ask_2

label Act_3_ask_1_answer_2:

    Monster "Tu penses vraiment pouvoir éteindre la lumière? Ma présence n’en rend ta chambre que plus lumineuse. Tu as quand même un sacré culot, mais tu n’ébranlera pas la confiance que j’ai en moi."
    Monster "Je fais craquer qui je veux, quand je veux. Tu ressembles d’ailleurs beaucoup à une cracotte."
    jump Act_3_ask_2

label Act_3_ask_1_answer_3:

    Monster "Celle là était un peu facile. Je viens juste te questionner sur ta façon de draguer. Pas de réaliser mes voeux, qui n’ont d’ailleurs aucun rapport avec toi. Je m'intéresse simplement à toi"
    jump Act_3_ask_2

label Act_3_ask_2:

    show monster

    Monster "On m’a toujours dit de suivre mes rêves. Alors ce soir j’ai décidé de te suivre. Tu m’as interloqué aujourd’hui. J’étais présent à chacun de tes rendez-vous."
    Monster "Je dois dire que tu as plutôt fait sensation forte à utiliser toutes ses phrases sorties d’on ne sait où. Mais je pense avoir percé ton secret."

    call device_appear
    menu:

        "{color=#ff78bb}69 \%{/color}\nTu crois vraiment?\n Je dirais plutôt\n que ton regard m’a transpercé\n et j’en ai le souffle coupé.\nMais je resterais une énigme pour toi.":
            hide device
            with dissolve
            show monster smile
            with dissolve
            jump Act_3_ask_2_answer_1 # ~

        "{color=#ff78bb}69 \%{/color}\nOui bon je l’avoue.\n Je triche, ça fait deux mois que\n je cherche des phrases\n toute faites sur Internet. Mais...\n j’ai l’impression de ne pas être le seul.":
            hide device
            with dissolve
            $ monster_love -= 20
            jump Act_3_ask_2_answer_2 # -

        "{color=#ff78bb}69 \%{/color}\nTu n’arriveras pas à ma cheville.\n J’ai un trop grand niveau de drague.\n J’ai maîtrisé cette technique et toi\n tu as tout juste l’air de débuter.":
            hide device
            with dissolve
            show monster wink
            with dissolve
            $ monster_love += 15
            jump Act_3_ask_2_answer_3 # +


label Act_3_ask_2_answer_1:

    Monster "Oh je pense que l’énigme est toute résolue. En attendant que tu arrives j’ai pu un peu regarder sur ton ordinateur les derniers sites que tu as {cps=5}visité...{/cps}"
    Monster "Il s’avère que tu as un sacré penchant pour les phrases de dragues un peu limites. Tes recherches devraient progresser nettement avec moi !"
    jump Act_3_ask_3

label Act_3_ask_2_answer_2:

    Monster "Effectivement, même pas besoin de te tirer les vers du nez. Il faudra quand même que tu apprennes le minimum syndical pour se faire désirer."
    Monster "Tu deviens la proie facile. Même pas besoin de sortir les crocs."
    jump Act_3_ask_3

label Act_3_ask_2_answer_3:

    Monster "Tu fais le présomptueux. J’aime ça ! Il faut quand même que tu saches que personne ne peut me battre sur le terrain de la séduction. Je suis un {size=+10}maître{/size} en la matière."
    Monster "Mais je veux bien commencer par ta \"cheville\" enflé pour ensuite remonter plus profondément en toi."
    jump Act_3_ask_3

label Act_3_ask_3:

    show monster
    with dissolve

    Monster "Malgré tout, le rejet peut conduire à un stress émotionnel pour les deux parties et le stress émotionnel peut conduire à des complications physiques tels que maux de tête, les ulcères, les tumeurs cancéreuses, et même la mort ! Donc, pour ma santé et la tienne, accepte de tomber dans mes bras !"

    call device_appear
    menu:

        "{color=#ff78bb}69 \%{/color}\nOh oui susurre moi des mots doux.\n Peut-être est-ce que je te laisserais\n une chance.":
            hide device
            with dissolve
            show monster smile
            with dissolve
            jump Act_3_ask_3_answer_1 # ~

        "{color=#ff78bb}69 \%{/color}\nJe pense être en assez bonne\n santé mentale et physique\n pour pouvoir te dire que\n je ne suis pas intéressé.":
            hide device
            with dissolve
            show monster wink
            with dissolve
            $ monster_love += 15
            jump Act_3_ask_3_answer_2 # +

        "{color=#ff78bb}69 \%{/color}\nEuh… D’accord !":
            hide device
            with dissolve
            jump Act_3_ask_3_answer_3 # -

label Act_3_ask_3_answer_1:

    Monster "Peut-être? Mais tu es déjà à mes pieds. N’inverse pas les rôles. Tu n’as pas encore les capacités pour jouer dans la cour des grands."
    Monster "Je pense que le sort est jeté de toute façon !"
    if monster_love >= 50:
        jump Act_3_Good_End
    else:
        jump Act_3_Bad_End

label Act_3_ask_3_answer_2:

    Monster "Mmh… Tu me résistes. Personne n’a réussi à tenir jusqu’ici. Je t’ai sous estimé, tu es plus doué que tu en avais l’air."
    Monster "Un homme désirable, plein d’assurance et qui ne se laisse intimider par rien ni personne. Ça te rend tellement sexy et affriandant ! J’en gouterais bien un morceau."
    jump Act_3_Good_End

label Act_3_ask_3_answer_3:

    Monster "Trop facile. Je t’ai dans mes filets. Un peu de résistance aurait été appréciable. Mais je me doutais que tu ne serais pas un challenge !"
    jump Act_3_Bad_End


label Act_3_Good_End:

    Player "Tu es mien !"
    stop music fadeout 1.0
    scene cg monster good
    with fade

    play audio [ "<silence .5>", "sound/cri.mp3" ]
    Player "J’aimerais t’inviter pour le week-end. Nous partons dans une heure. Je te montrerai la ville, on mangera bien, on boira du bon vin et on fera l’amour."

    jump credit


label Act_3_Bad_End:

    stop music fadeout 1.0
    scene cg monster bad
    with fade

    play audio [ "<silence .5>", "sound/tentacles.mp3" ]
    Narrator "Vous avez succombé a la Tentacle ..."

    jump credit

label credit:

    scene bg end
    with fade

    pause 5.0

    Narrator "Fun Fact : la majorité des répliques utilisés ont été inspiré d'internet !"

    scene bg end
    pause 5.0

    return
