---
layout: page
---
<style>
    p {
        margin-left: 10px;
    }
    #outer {
        display: grid;
        grid-template-columns: auto auto auto;
        gap: 0;
        flex-wrap: wrap;
        align-items: center;
    }
    .child {
        background-color: white;
        padding: 25px;
        font-size: 42px;
        text-align: center;
    }
    .child img {
        width: 120px;
        object-fit: cover;
    }
    #marc {
        width: auto;
        height: 48px;
    } 
    #bib {
        width: auto;
        height: 48px;
    }
    #dacs {
        color: darkblue;
        font-weight: bolder;
        font-style: italic;
    }
</style>

<div id="outer">
<div class="child"><img src="/docs/bibframe-newlogo.jpg" id="bib"></div>
<div class="child"><img src="/docs/rda.png"></div>
<div class="child"><img src="/docs/ead.png"></div>
<div class="child" id="dacs">DACS</div>
<div class="child"><img src="/docs/mods.png"></div>
<div class="child"><img src="/docs/marc21.png" id="marc"></div>
</div>

# Metadata & Cataloging
## Modeling Works in BIBFRAME
<p>BIBFRAME, the works cataloging ontology from Library of Congress, promises to improve catalog accessibility and accuracy by storing metadata as linked data. In the below examples, I show the results of my effort to effectively catalog  as BIBFRAME the Hackett Publishing instance of the Tao Te Ching, which is an original translation. The existing entries at id.loc.gov have several problems: a later version of the work, published by Shambala, is listed as a separate work with its own instance rather than a new instance of the same work; several discrepancies exist between the two work entries; neither work refers to the appropriate work hub, that is, the original Chinese text.
 </p>
  * [Work on id.loc.gov linked to Hackett instance](https://id.loc.gov/resources/works/2050961.html)<br>
  * [Work on id.loc.gov linked to Shambala instance](https://id.loc.gov/resources/works/14802384.html)<br>
  * [Tao Te Ching hub on id.loc.gov](https://id.loc.gov/resources/hubs/42abf244-bec0-a8f9-beeb-828bd5338bb7.html)
 
<p>My updated work/instance file below more thoroughly describes the work and Hackett instance. The work description would replace the two existing works on id.loc.gov, the LOC Hackett instance would be updated to match mine, and both the Hackett and Shambala instances would be linked to my new work description. </p>

 * [Improved Tao Te Ching Work/Instance, BIBFRAME](/docs/bibframe_taoteching_rdf.txt) 

## Modeling Name Authority in MADS, SKOS & BIBFRAME
<p>While analyzing the links for my Tao Te Ching entry, it was clear that the authority entry for Stephen Addiss, the artist and translator who worked on the book, needed additional information. In particular, there are no links to his most well-known works, including the Tao Te Ching. I used the BIBFRAME Extension (bflc) vocabulary to record references to these works to enhance description and information retrieval.</p>

 * [Stephen Addiss Authority Record on id.loc.gov](http://id.loc.gov/authorities/names/n78009070)<br>
 * [Enhanced Stephen Addiss Authority Record](/docs/Addiss_Stephen_rdf.txt)

## Digital Archiving with DACS/EAD
<p>I created this archive of Alan Justad's emails for Seattle Municipal archives. I used ePADD software to initially organize the thousands of emails using machine learning functionality, performed weeding and other manual reorganization activities, and described its series and sub-series prior to publishing using DACS/EAD.</p>

 * [Department of Planning and Development Director's Office Correspondence](http://archives.seattle.gov/finding-aids/repositories/2/resources/1840)

## Institutional Data Project Metadata Standard, San Diego State University
<p>I was on a team of librarians that adapted and refined metadata standards for SDSU's Institutional Data Project, part of the LOC's Program for Cooperative Cataloging. We created proxy authority records for SDSU faculty. I applied the standard to hundreds of Wikidata authority records and made recommendations for modifications based on existing Wikidata property definitions and available source data. The below page also contains links to several SPARQL queries I wrote that extract data and statistics from the Wikidata record set. </p>
 
 * [Metadata Standard Project Page](https://www.wikidata.org/wiki/Wikidata:WikiProject_PCC_Wikidata_Pilot/San_Diego_State_University/SDSU_Institutional_Data_Project)

## Traditional Metadata Encodings
<p>Here are some example of resource descriptions I've done using traditional encoding standards.</p>
 * [Dublin Core - Tao Te Ching](/docs/dc_taoteching.xml)<br>
 * [EAD - African American Soldier Portrait](/docs/ead_afamericansoldier.xml)<br>
 * [MARC - "Winning Letters" Book Series](/docs/marc_winningletters.txt)



