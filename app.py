import streamlit as st
from rdflib import Graph

# Our competency question (real-data based)
CQ_TEXT = (
    "Who won the Gold medal in the Men's 100 metres Butterfly event at the "
    "2008 Beijing Summer Olympics, and which country did he represent?"
)

SPARQL_QUERY = """
PREFIX olympics: <http://olympic-data.org/ontology#>
PREFIX resource: <http://olympic-data.org/resource/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?athleteName ?countryName ?eventName ?year
WHERE {
  ?athlete a olympics:Athlete ;
           olympics:athleteName ?athleteName ;
           olympics:representsCountry ?country ;
           olympics:wonMedal ?medalResult .

  ?country olympics:countryName ?countryName .

  ?medalResult olympics:medalType "Gold" ;
               olympics:forEvent ?event ;
               olympics:atGame ?game .

  ?event olympics:eventName ?eventName ;
         olympics:belongsToSport ?sport .

  ?sport olympics:sportName "Swimming" .

  ?game olympics:year ?year ;
        olympics:season "Summer" ;
        olympics:hostCity "Beijing" .
}
"""


@st.cache_resource
def get_graph():
    g = Graph()
    g.parse("olympic-ontology.ttl", format="turtle")
    g.parse("olympic-data.ttl", format="turtle")
    return g

def run_query():
    g = get_graph()
    results = g.query(SPARQL_QUERY)

    rows = []
    for r in results:
        rows.append(
            {
                "Athlete": str(r["athleteName"]),
                "Country": str(r["countryName"]),
                "Event": str(r["eventName"]),
                "Year": str(r["year"]),
            }
        )
    return rows

def main():
    st.title("Olympic Demo")

    # Show the competency question on screen
    st.write("Competency question:")
    st.write(f"**{CQ_TEXT}**")
    st.write("Copy the same competency question to ask your question section....")

    # Empty input (professor khud likhega)
    user_q = st.text_input("Ask your question:")

    if st.button("Get answer"):
        if not user_q.strip():
            st.warning("Please enter a question.")
            return

        rows = run_query()

        if not rows:
            st.info("No answer found in the current data.")
        else:
            st.write("Answer:")
            st.table(rows)

if __name__ == "__main__":
    main()
