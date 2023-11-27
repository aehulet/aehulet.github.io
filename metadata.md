---
layout: page
---
<style>
    p {
        margin-left: 10px;
    }
</style>
# Metadata & Cataloging
## Modeling Works in BIBFRAME
<p>BIBFRAME, the works cataloging ontology from Library of Congress, promises to improve catalog accessibility and accuracy by storing metadata as linked data. In the below examples, I show the results of my effort to effectively catalog  as BIBFRAME the Hackett Publishing instance of the Tao Te Ching, which is an original translation. The existing entries at id.loc.gov have several problems: a later version of the work, published by Shambala, is listed as a separate work with its own instance rather than a new instance of the same work; several discrepancies exist between the two work entries; neither work refers to the appropriate work hub, that is, the original Chinese text.
 </p>
  * [Work on id.loc.gov linked to Hackett instance](https://id.loc.gov/resources/works/2050961.html)<br>
  * [Work on id.loc.gov linked to Shambala instance](https://id.loc.gov/resources/works/14802384.html)<br>
  * [Tao Te Ching hub on id.loc.gov](https://id.loc.gov/resources/hubs/42abf244-bec0-a8f9-beeb-828bd5338bb7.html)
 
<p>My updated work/instance file below more thoroughly describes the work as recorded in the Hackett instance. The work description would replace the two existing works on id.loc.gov, and both the LOC Hackett instance and the Shambala instance would be linked to it. </p>

 * [Improved Tao Te Ching Work/Instance, BIBFRAME](/docs/bibframe_taoteching.rdf) 

## Modeling Name Authority in MADS, SKOS & BIBFRAME
<p>While analyzing the links for my Tao Te Ching entry, it was clear that the authority entry for Stephen Addiss, the artist and translator who worked on the book, needed additional information. In particular, there are no links to his most well-known works, including the Tao Te Ching. I used the BIBFRAME Extension (bflc) vocabulary to record references to these works to enhance description and information retrieval.</p>

 * [Stephen Addiss Authority Record on id.loc.gov](http://id.loc.gov/authorities/names/n78009070)<br>
 * [Enhanced Stephen Addiss Authority Record](/docs/Addiss_Stephen.rdf)

## Digital Archiving with DACS/EAD
<p>I created this archive of Alan Justad's emails for Seattle Municipal archives. I used ePADD software to initially organize the thousands of emails using machine learning functionality, performed weeding and other manual reorganization activities, and described its series and sub-series prior to publishing using DACS/EAD.</p>

 * [Department of Planning and Development Director's Office Correspondence](http://archives.seattle.gov/finding-aids/repositories/2/resources/1840)

## Traditional Metadata Encodings
<p>Here are some example of resource descriptions I've done using traditional encoding standards.</p>
 * [Dublin Core - Tao Te Ching](/docs/dc_taoteching.xml)<br>
 * [EAD - African American Soldier Portrait](/docs/ead_afamericansoldier.xml)<br>
 * [MARC - "Winning Letters" Book Series](/docs/marc_winningletters.txt)



