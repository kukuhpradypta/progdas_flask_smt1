from flask import jsonify, request, json, session, redirect

from app.api.db_service import execute_query
from . import list


@list.route('/api/list/getTest', methods=['GET'])
def getTest():
    return 'test'
    # try:
    #     # Memperbarui kueri untuk mengambil center_lat dan center_lon
    #     select_country = """
    #         SELECT 
    #             country_name,
    #             ST_AsGeoJSON(wkb_geometry) AS country_border,
    #             center_lat,
    #             center_lon
    #         FROM 
    #             ref_country
    #         WHERE 
    #             ST_AsGeoJSON(wkb_geometry) IS NOT NULL;
    #         """
    #     country_result = execute_query(select_country, 'db_marivision')
    #     if not isinstance(country_result, list):
    #         return country_result

    #     select_budget = """
    #         SELECT 
    #             category, 
    #             value, 
    #             b.country_name 
    #         FROM 
    #             gfp_financials 
    #         INNER JOIN 
    #             gfp_country b 
    #         ON 
    #             b.cty_id = gfp_financials.cty_id
    #         """
    #     budget_result = execute_query(select_budget, 'db_marivision')
    #     if not isinstance(budget_result, list):
    #         return budget_result
    #     else:
    #         # Mengubah hasil kueri menjadi format yang diinginkan
    #         country_dict = {}
    #         for country_name, geom, center_lat, center_lon in country_result:
    #             country_dict[country_name] = {
    #                 "geom": geom,
    #                 "center_lat": center_lat,
    #                 "center_lon": center_lon,
    #                 "budget": []
    #             }
            
    #         for category, value, country_name in budget_result:
    #             if country_name in country_dict:
    #                 if value is not None and value != "":  # Memastikan value tidak kosong
    #                     country_dict[country_name]["budget"].append({
    #                         "category": category,
    #                         "value": value,
    #                         "country_name": country_name
    #                     })
            
    #         final_result = [
    #             {"country_name": country, **data} 
    #             for country, data in country_dict.items() 
    #             if data["budget"]
    #         ]
            
    #         return jsonify({"status": "ok", "output": final_result}), 200
        
    # except Exception as err:
    #     return jsonify({"status": "failed", "message": str(err)}), 200
