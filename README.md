## Intro
A repository to host details of many festivals/observances of Indian hindus

## Categorization
### Repositories
- Festivals are divided into different repositories, which are identified by paths. Example: tamil, temples/Tamil, temples/North, gRhya/general, mahApuruSha/kAnchI-maTha.
- Motivation: Not everyone is interested in every festival: example: A vaiShNava person from karNATaka may not care for a tamil nAyanAr gurupUjA. 
- Metadata about repositories are stored in repos.toml in the root of this github repo.

### Path within repository
- Each festival gets one TOML file.
- Within each repository, the path of a given festival is decided by its timing information. This facilitates easy lookup.
- Paths for independently determined festivals: `[repository_root]/[month_type]/[anga_type]/[month_num]/[anga_num]/[festival_id].toml` , where month_type is one of `[lunar_month, solar_sidereal_month, tropical_month]`, and anga_type is one of `[day, tithi, nakshatra, yoga, karana]`.
- Paths for relatively determined festivals: `[repository_root]/[anchor_festival_id]/offset__[day]/[festival_id].toml` , where offset `day` may be negative.
- There is provision for giving information about festivals without specifying timing (because complicated timing is more easily specified as code). In such a case, path will be `[repository_root]/description_only/[arbitrary_path]/[festival_id].toml`.

One can run the below python code to fix the path automatically:

```
from jyotisha.panchaanga.temporal.festival.rules import RulesCollection
rules_collection = RulesCollection.get_cached(repos_tuple=rule_repos, julian_handling=None)
rules_collection.fix_filenames()
```

## Field values
- Please don't use "/" or space in id field value. Causes problems with deciding canonical file path; and makes command line operation ugly.
- Where possible, please try to ensure that filename matches id field. (This will be periodically enforced anyway with scripts.)
- Long string fields (such as description) allow markdown, enriched with comments marked as `+++(some comment)+++`. It is up to consumers to convert this appropriately for presentation to users.

### Extra timing information
- Basic information about festival timing is covered in the "Path within repository" section.
- Festivals are associated with kaala-s (time intervals), which may be one of `प्राक्तनारुणोदयः`, `सूर्योदयः`, `सूर्यास्तमयः`, `चन्द्रोदयः`, `पूर्वाह्णः`, `अपराह्णः` etc.. The default kaala is assumed to be `सूर्योदयः`. An `anga` (such as `tithi`) intersecting with an appropriate kaala determines a "festival".
- Such an intersection may happen on two consecutive days. In that case, the priority field (with values being one of `puurvaviddha, paraviddha, vyaapti`) determines the day to be chosen for the "festival".

#### Clarity about meaning of kaala values
- `प्राक्तनारुणोदयः` refers to the dawn _preceding_ a given day.

## Language and script
- Names can be provided in a variety of languages. Please use the best/ common script for the language (usually the native script). 
  - Exception to the above: Tamil names are stored in HK (because the latter differentiates between vargIya consonants!)
