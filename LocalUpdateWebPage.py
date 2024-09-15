"""Script updating the distribution webpage with links to current distributions.  
"""
import osmapa.www

osmapa.www.refresh_index_html(
    product_dir="/mnt/h/MySVN/Projekty/OSM/git/las-osmapa-garmin/products", 
    product_list=[
        "OSMapaPL-PODSTAWOWA", 
        "OSMapaPL-OGONKI", 
        "OSMapaPL-LIGHT", 
        "OSMapaPL-WARSTWICE", 
        "OSMapaPL-SZLAKI",
        "OSMapaPLext-PODSTAWOWA", 
        "OSMapaPLext-OGONKI", 
        "OSMapaPLext-LIGHT", 
        "OSMapaPLext-WARSTWICE", 
        "OSMapaPLext-SZLAKI",
        ], 
    template_file="/mnt/h/MySVN/Projekty/OSM/git/las-osmapa-garmin/www/TEMPLATE_index.html", 
    target_file="/mnt/h/MySVN/Projekty/OSM/las-osmapa-garmin-www/index.html",
    verbose=True)
