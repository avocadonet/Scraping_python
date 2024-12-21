from flask import Flask, request, render_template
import backend.parser_all.parser_chipdip as parser_chipdip
import backend.parser_all.parser_elecomp as parser_elecomp
import database.sql as sql
import logging

app = Flask(__name__,
            template_folder='../frontend/')
    
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sql.init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    elecomp_results = []
    chipdip_results = []
    search_query = None

    if request.method == "POST":
        search_query = request.form.get("search_query")
        
        if search_query:
            try:
                elecomp_results = sql.get_results_from_db(search_query, source="elecomp")
                chipdip_results = sql.get_results_from_db(search_query, source="chipdip")

                logger.info(f"elecomp_results from DB: {elecomp_results}")
                logger.info(f"chipdip_results from DB: {chipdip_results}")

                if not elecomp_results:
                    elecomp_results_parsed = parser_elecomp.search_products(search_query)
                    if isinstance(elecomp_results_parsed, list):
                        elecomp_results = elecomp_results_parsed
                        sql.save_results_to_db(search_query, elecomp_results, source="elecomp")

                if not chipdip_results:
                    chipdip_results_parsed = parser_chipdip.search_products(search_query)
                    if isinstance(chipdip_results_parsed, list):
                        chipdip_results = chipdip_results_parsed
                        sql.save_results_to_db(search_query, chipdip_results, source="chipdip")
            
            except Exception as e:
                logger.error(f"[ERROR] Произошла ошибка: {e}")

    if (search_query == None):
        return render_template("website.html", 
                           elecomp_results=elecomp_results, 
                           chipdip_results=chipdip_results, 
                           search_query="Радио")
        
    return render_template("website.html", 
                           elecomp_results=elecomp_results, 
                           chipdip_results=chipdip_results, 
                           search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)