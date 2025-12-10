My current competency question is:

**“Who won the Gold medal in the Men's 100 metres Butterfly event at the 2008 Beijing Summer Olympics, and which country did he represent?”**

-> I modeled this exactly in my RDF data: Michael Phelps, representing USA, in the Swimming Men's 100m Butterfly event at the 2008 Beijing Summer Games.

-> The ontology (olympic-ontology.ttl) defines the schema:  Athlete, Country, Sport, Event, OlympicGame, MedalResult
   properties like:  representsCountry, wonMedal, forEvent, atGame, sportName, eventName, year, season, hostCity, medalType.

-> The RDF file (olympic-data.ttl) contains a real example instance following this schema.

-> In the Streamlit app, when someone types this question and clicks “Get answer”, a SPARQL query is executed on the RDF graph and returns the real answer from the data, not hard-coded text.
