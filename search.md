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
        font-size: 24px;
        text-align: center;
    }
    .child span {
        vertical-align: top;
    }
    .child img {
        object-fit: cover;
    }
</style>

<div id="outer">
<div class="child"><img src="/docs/python.png" width="76" height="76"><span> Python</span></div>
<div class="child"><img src="/docs/js.png" width="76" height="76"><span> JavaScript</span></div>
<div class="child"><img src="/docs/django.png" width="76" height="76"><span> Django</span></div>
<div class="child"><img src="/docs/rdf.png" width="72" height="76"><span> RDF</span></div>
<div class="child"><img src="/docs/sparql.png" width="76" height="76"><span> SPARQL</span></div>
<div class="child"><img src="/docs/sql2.png" width="76" height="76"><span> SQL</span></div>
</div>

# Technical Work Examples
## Search & Discovery with Wikiframe Visual Graph
<p>I am the project developer for WikiframeVG, which is a linked data search & discovery application for the Wikidata Knowledge Graph, one of the world's largest. I manage the project in conjunction with Darnelle Melvin and Cory Lampert, both of the University of Nevada-Las Vegas, which provided funding for the effort.</p>
<p>WikiframeVG allows organizations and project teams to set the scope of the data that the application searches. This is a critical feature, since Wikidata contains billions of statements, which become an impediment to efficient search in some instances. The prototype version (link below) allows users to search UNLV special collections data. Wikiframe combines traditional keyword and faceted search with semantic search made possible with linked data stores. The application graphs relationships between all search results, and users interact with the graph to search based on defined entity values, such as a person's occupation. Wikiframe also creates geographical maps of results when location data are present.</p>

 * [WikiframeVG website](https://wikiframe.library.unlv.edu)
 * [WikiframeVG github repository](https://github.com/UNLV-Libraries/wikidata-discovery-project)

## WikiframeVG Requirements Development
<p>I functioned as a business analyst for the Wikiframe project as well. My requirements development approach expresses business requirements as high-level feature descriptions, to which functional and technical requirements are traced. I also cite the code modules that comprise the features so that developers know how to navigate the source code.</p>

 * [Requirements development site](https://github.com/UNLV-Libraries/wikidata-discovery-project/wiki)

## Querying with SPARQL
<p>Understanding the SPARQL query language is increasingly important for technologists and metadata professionals as linked data platforms and applications spread. The example I provide here concisely instructs the Wikidata Query Service to retrieve all property data -- including property qualifiers -- for any given item. Due to the looser structure of knowledge graph triple stores, requesting data from various parts of the graph can require a lot of statements. This example exploits Wikidata namespaces for statements, properties, and property qualifiers to return all data for a given item, no matter its properties or particular structure, in just a few lines of code.</p>

 * [Link to query in Wikidata query window](https://w.wiki/8G5b)
 * [SPARQL statement for Wikidata Item](/docs/item_sparql.txt)

## Data Processing with SQL & Python
<p>Data processing workflows are a critical aspect of data management; data must be routinely retrieved, updated, transformed, transmitted, extracted, or loaded, depending on the situation. In this example, I wrote SQL stored procedures for managing reporting data that must be cached and managed via the Wikidata Query Service. The accompanying Python script implements the workflow that retrieves the data, logs into the database, saves current report data to a history table, truncates the active report table, and inserts the new data.</p>

 * [SQL Stored procedures](/docs/cache_report_data_sql.txt)
 * [Data processing script - python](/docs/get_stats_py.txt)

