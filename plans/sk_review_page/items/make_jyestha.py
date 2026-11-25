import json, tomllib, glob, os
ROOT = '/home/user/adyatithi'
def find(i):
    for f in glob.glob(ROOT + '/**/*.toml', recursive=True):
        try: d = tomllib.load(open(f, 'rb'))
        except Exception: continue
        if d.get('id') == i: return os.path.relpath(f, ROOT), d
    raise SystemExit('no ' + i)
END = '---स्मृतिकौस्तुभे'
items = []
def add(doc, i, after, ref, note, replace_ref=None):
    f, d = find(i)
    refkey = 'references_primary' if 'references_primary' in d else 'references_secondary'
    it = dict(doc=doc, key='sh:' + i, id=i, file=f, existing=d.get('shlokas', '').strip('\n'),
              after=(after.strip('\n') + '\n' + END) if after.strip() else '', ref=ref, refkey=refkey, note=note)
    if replace_ref: it['replace_ref'] = replace_ref
    items.append(it)

add('j-jyaiShTha-mAsa-ArambhaH', 'jyaiShTha-mAsa-ArambhaH', '''
निर्णयामृते भविष्ये---
पिष्टेन कञ्जं कृत्वा ज्येष्ठे मासि सवेदिकम्।
पुष्पैः संपूज्य गन्धाढ्यैर्नानावस्त्रविभूषणैः॥
वर्षकोट्ययुतं सायं सूर्यलोके महीयते॥
(कञ्जो ब्रह्मा।)
तत्रैव वामनपुराणे---
उदकुम्भाम्बु धेनुं च तालवृन्तं सचन्दनम्।
त्रिविक्रमस्य प्रीत्यर्थं दातव्यं ज्येष्ठमासि वा॥
''', 'Smriti Kaustubham p.117',
"Both verses are already here from Puruṣārtha-cintāmaṇi, in a different reading (कञ्जजं / कञ्जं, वर्षकोटिशतं साग्रं / वर्षकोट्ययुतं सायं, धेनुश्च / धेनुं च, च / वा). SK's reading is offered as a second witness; reject the text and keep only the reference if you prefer. SK's footnote reads स्वर्गलोके for सूर्यलोके.")

add('j-karavIra-vratam', 'karavIra-vratam', '''
मदनरत्ने भविष्योत्तरे---
ज्येष्ठे मासि सिते पक्षे प्रथमेऽह्नि दिनोदये।
देवोद्यानभवं हृद्यं करवीरं समर्चयेत्॥
रक्ततन्तुपरीधानगन्धधूपविलेपनैः।
प्ररूढसप्तधान्यैश्च नारङ्गैर्बीजपूरकैः॥
गुणकैर्बदरैर्भक्ष्यैर्[?] नारिकेलैः सुशोभनैः।
अभ्युक्ष्याक्षततोयेन मन्त्रेणेत्थं क्षमापयेत्॥
करवीर विषावास नमस्ते भानुवल्लभ।
मौलिमण्डन दुर्गादिदेवानां सततं प्रिय॥
आकृष्णेनेति वेदोक्तमन्त्रेणाभ्यर्च्य भक्तितः।
एवं भक्त्या समभ्यर्च्य दत्त्वा विप्राय दक्षिणाम्॥
प्रदक्षिणत्रयं कुर्यात्ततः स्वभवनं व्रजेत्।
करवीरव्रतं पार्थ सर्वसौख्यफलप्रदम्॥
''', 'Smriti Kaustubham p.117',
"The existing mantra reads दम्भोलिमृडदुर्गादि where SK has मौलिमण्डन दुर्गादि; SK's whole mantra is added. [?] on गुणकैर्बदरैर्भक्ष्यैर् (OCR गुणकैबंदर्भक्ष्यै). The list of women who kept the vrata and the closing vasantatilakā verse are left out.")

add('j-rambhA-tRtIyA', 'rambhA~tRtIyA', '''
निर्णयामृते भविष्योत्तरे---
ज्येष्ठशुक्लतृतीयायां स्नाता नियमतत्परा।
कुरु पार्श्वेषु पञ्चाग्नीन्ज्वलमानान्हुताहुतीन्॥
गार्हपत्यं दक्षिणाग्निं सभ्यं चाहवनीयकम्।
पञ्चमं भास्करं तेज इत्येते पञ्च वह्नयः॥
एतेषां मध्यमा भूत्वा तिष्ठ पूर्वमुखी स्थिरा।
चतुर्भुजां ध्यानपरां पङ्कजासनसंस्थिताम्॥
महालक्ष्मी महाकाली महामाया महामही।
महानना महादेवी महामहिषमर्दिनी॥
गङ्गा च यमुना चैव शतद्रुर्नर्मदा तथा।
सरस्वती वैतरणी सैव प्रोक्ता महासती॥
सप्रणवैर्नमोन्तैश्च नामभिः पूजनं भवेत्।
चतुर्थीसहितैश्चैव स्वाहान्तहोम इष्यते॥
स्त्रीणां चातुलसौभाग्यं गार्हस्थ्यं सार्वकामिकम्।
सपत्नीदर्पदलनं वशीकरणमुत्तमम्॥
मृता शिवपुरं याति ततो विष्णुपुरं व्रजेत्॥
''', 'Smriti Kaustubham p.117-119',
"The entry already has SK's pūjā verses (p.118) and the pūrvaviddhā rule; this adds the opening (five fires), the names used in the pūjā and the phala. Widens the existing p.118 reference. SK's footnote attributes the passage to the Devī-purāṇa.",
replace_ref='Smriti Kaustubham p.118')

add('j-umA-avatAraH', 'umA-avatAraH', '''
मदनरत्ने ब्रह्मपुराणे---
उपहारैश्च विविधैर्गीतनृत्योत्सवादिभिः।
होमैः पयोभिर्वस्त्रैश्च पत्रपुष्पैः सुगन्धिभिः॥
''', 'Smriti Kaustubham p.119',
"The entry's verse is exactly SK's first verse; this adds the verse that follows it in SK (how to worship), under SK's attribution.")

add('j-zukla-dEvI-pUjA', 'zukla-dEvI-pUjA', '''
निर्णयामृते देवीपुराणे---
शुक्लाष्टम्यां पुरा जाता शुक्लादेवी महाशनिः।
वधाय दानवेन्द्राणां शुक्लपक्षेऽथ तां यजेत्॥
''', 'Smriti Kaustubham p.119',
"Timing disagreement: SK puts Śuklā-devī on the aṣṭamī (शुक्लाष्टम्यां); this entry is on Jyeṣṭha śukla navamī (03/09). Verse added, timing left unchanged.")

add('j-brahmANI-pUjA', 'brahmANI-pUjA', '''
निर्णयामृते भविष्ये---
उपवासपरो भक्त्या नवम्यां पूजयेदुमाम्।
ब्रह्माणीमिति वै नाम्ना श्वेतरूपेण रूपिणीम्॥
ज्येष्ठे मासि नृपश्रेष्ठ कृत्वा नक्तस्य वै विधिम्।
शाल्यन्नपायसोपेतं स्वयं भुञ्जीत वाग्यतः॥
कुमारीर्[?] भोजयेच्चापि स्वशक्त्या ब्राह्मणांस्तथा॥
''', 'Smriti Kaustubham p.119',
"[?] on कुमारीर् (OCR कुमारी). In SK Brahmāṇī is Umā worshipped in white form, while the description calls her one of the seven mātṛkās. SK's footnote reads ब्रह्मपुराणे for भविष्ये, also marked [?].")

add('j-dazaharA', 'dazaharA_or_gaGgAvataraNam_or_dazapApaharA~dazamI', '''
निर्णयामृते स्कान्दे---
ज्येष्ठे मासि सिते पक्षे दशम्यां बुधहस्तयोः।
व्यतीपाते गरानन्दे कन्याचन्द्रे वृषे रवौ॥
दशयोगे नरः स्नात्वा सर्वपापैः प्रमुच्यते॥
(दिनद्वयेऽपि कतिपययोगवद्दशमीसत्त्वे गङ्गापूजनादौ दैवे कर्मणि पूर्वाह्णस्य पुण्यकालत्वात्तद्व्यापिन्येव दशमी ग्राह्या।)
हेमाद्रौ---
गङ्गास्नाने कृतार्थः स्यात्तस्मिन्योगे सकृन्नरः।
हरेद्वै [?] दश पापानि गङ्गा तत्र न संशयः॥
काशीखण्डे---
दशाश्वमेधिके स्नात्वा मुच्यते सर्वपातकैः।
लिङ्गं दशाश्वमेधेशं दृष्ट्वा दशहरातिथौ॥
दशजन्मार्जितैः पापैस्त्यज्यते नात्र संशयः॥
नमः शिवायै प्रथमं नारायण्यै पदं ततः।
दशहरायै पदमिति गङ्गायै मन्त्र एष वै॥
स्वाहान्तः प्रणवादिश्च भवेद्विंशाक्षरो मनुः।
पूजा दानं जपो होमस्तेनैव मनुना स्मृतः॥
स्कान्दे---
ज्येष्ठस्य शुक्लदशमी संवत्सरमुखी स्मृता।
तस्यां स्नानं प्रकुर्वीत दानं चैव विशेषतः॥
ज्येष्ठे मासि सिते पक्षे दशमी हस्तसंयुता।
संहरेत्त्रिविधं पापं बुधवारेण संयुता॥
तस्यां दशम्यामेतच्च स्तोत्रं गङ्गाजले स्थितः।
यः पठेद्दशकृत्वस्तु दरिद्रो वापि चाक्षमः॥
सोऽपि तत्फलमाप्नोति गङ्गां संपूज्य यत्नतः॥
''', 'Smriti Kaustubham p.119-122',
"The entry already has the कुजे दिने / हस्तर्क्षे verse (reading तु, मासे) and यां काञ्चित्सरितं प्राप्य…, so those are not repeated; SK adds the daśa-yoga verse, Hemādri, the Kāśī-khaṇḍa verses and Gaṅgā mantra, and the stotra's phala verses. The 36-verse Daśaharā-stotra itself (pp.120–122) is left out as too long; say if you want it. [?] on हरेद्वै. Timing: SK takes the pūrvāhṇa-vyāpinī daśamī (and rejects counting yogas); the entry sets no kaala. Unchanged.")

add('j-vaTa-pUrNimA', 'vaTa-pUrNimA_or_vaTa-sAvitrI-vratam', '''
स्कान्दे---
ज्येष्ठे मासि सिते पक्षे पौर्णमास्यां तथा व्रतम्।
चीर्णं पुरा महाभक्त्या कथितं ते मया नृप॥
(अस्मिंश्च व्रते पूर्णमास्यमावास्ययोर्देशभेदेन यथाचारं व्यवस्था। तिथिद्वैधे चतुर्दशीविद्धे एव ते ग्राह्ये।)
पराशरः---
ज्येष्ठशुक्लचतुर्दश्यां सावित्रीमर्चयन्ति याः।
वटमूले सोपवासा न ता वैधव्यमाप्नुयुः॥
निर्णयामृते भविष्योत्तरे---
अमायां च तथा ज्येष्ठे वटमूले महासती।
त्रिरात्रोपोषिता नारी विधिनानेन पूजयेत्॥
अशक्ता तु त्रयोदश्यां नक्तं कुर्याज्जितेन्द्रिया।
अयाचितं चतुर्दश्याममायां समुपोषणम्॥
दान-मन्त्रः---
सावित्रीयं मया दत्ता सहिरण्या महासती।
ब्रह्मणः प्रीणनार्थाय ब्राह्मण प्रतिगृह्यताम्॥
स्कान्दे वटसेचनम्---
वट सिञ्चामि ते मूलं सलिलैरमृतोपमैः।
सूत्रेण वेष्टये भक्त्या गन्धपुष्पाक्षतैः शुभैः॥
नमो वैवस्वतायेति कुर्याच्चैव प्रदक्षिणाम्॥
न्यग्रोध-नमस्कारः---
नमोऽव्यक्तस्वरूपाय महाप्रणवरूपिणे।
महदसोपविष्टाय [?] न्यग्रोधाय नमोऽस्तु ते॥
अर्घ्य-मन्त्रः---
ओंकारपूर्वके देवि सर्वदुःखनिवारिणि।
वेदमातर्नमस्तुभ्यमवैधव्यं प्रयच्छ मे॥
पतिव्रते महाभागे चन्द्रजाते शुचिस्मिते।
दृढव्रते दृढमते भर्तुश्च प्रियवादिनि॥
प्रार्थना---
सावित्रि ब्रह्मगायत्रि सर्वदा प्रियभाषिणि।
तेन सत्येन मां पाहि दुःखसंसारसागरात्॥
अवियोगो यथा देवि ब्रह्मणा सहितस्तव।
अवियोगस्तथास्माकं भूयाज्जन्मनि जन्मनि॥
''', 'Smriti Kaustubham p.124-128',
"Timing disagreement: SK lets custom choose pūrṇimā or amāvāsyā, takes either caturdaśī-viddhā, and gives Parāśara's caturdaśī form; the entry is plain 03/15 with no priority. Unchanged. The existing वट सिञ्चामि line continues differently there; SK's arghya verse 3 (अवैधव्यं च सौभाग्यं…) is already present in a variant, so it is not repeated. [?] on महदसोपविष्टाय. Left out: the pūjā upacāra mantras, the kathā (pp.128–134) and the udyāpana with the Yama arghya and twelve Yama names (pp.134–137).")

add('j-mahA-jyaiSThI-yOgaH', 'mahA-jyaiSThI-yOgaH', '''
ज्योतिःशास्त्रे---
ऐन्द्रे गुरुः शशी चैव प्राजापत्ये रविस्तथा।
पौर्णिमा ज्येष्ठमासस्य महाज्येष्ठी प्रकीर्तिता॥
(ऐन्द्रं ज्येष्ठा, प्राजापत्यं रोहिणी। अतः स्नानादौ तादृशयोगसंकीर्तनं कार्यम्।)
''', 'Smriti Kaustubham p.137',
"SK's definition (Jupiter and the moon in Jyeṣṭhā, the sun in Rohiṇī) differs from the description's 'Jyeshtha nakshatra on a Thursday'. Description and timing left unchanged; the gloss in parentheses is mine plus SK's sentence.")

add('j-manvAdiH-14', 'manvAdiH~(bhautyaH~[14])', '''
ज्येष्ठपौर्णमास्याम्---
अस्यामेव पौर्णमास्यां मन्वादित्वादपिण्डं श्राद्धमपि कर्तव्यम्।
''', 'Smriti Kaustubham p.137',
"Prose, not a verse: SK says the Jyeṣṭha pūrṇimā, being a manvādi, takes a piṇḍa-less śrāddha. Approve as is, or clear the text to add only the reference.")

json.dump(items, open('items-jyestha.json', 'w'), ensure_ascii=False, indent=1)
print(len(items), [i['file'] for i in items])
