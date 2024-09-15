"""Processor for HTML files.

Author: Andrzej Talarczyk <andrzej@talarczyk.com>

Based on work of Michał Rogalski (Rogal).

License: GPLv3.
"""

import subprocess
from shutil import move

def refresh_index_html(product_dir, product_list, template_file, target_file, verbose = False):
    """Find latest versions of map products and produce a correct index.html file from template. 

    Args:
        products_dir (string): directory where products are located
        product_list (array of string): a list of product names (e.g. "FAMILY-PRODUCT" in FAMILY-PRODUCT-[YYYYMMDD]V[VERSION].exe)
        template_file (string): source index.html file with placeholder tags ([YYYYMMDD] and [VERSION])
        target_file (string): target index.html file to be (over)written after tags have been replaced with values. 
    """

    # Read template.
    with open(template_file, 'r') as f:
        contents = f.read()

    for prod in product_list:
        prod_split = prod.split("-")
        latest_p_exe = get_latest_product(family=prod_split[0], product=prod_split[1], product_suffix="*.exe", product_dir=product_dir)
        latest_p_img = get_latest_product(family=prod_split[0], product=prod_split[1], product_suffix="*_IMG.zip", product_dir=product_dir)

        if verbose:
            print("latest_p_exe: " + latest_p_exe + ", latest_p_img: " + latest_p_img)
            
        if latest_p_exe != None and latest_p_exe != "":
            contents = contents.replace(prod+"-[YYYYMMDD]V[VERSION].exe", latest_p_exe)
        if latest_p_img != None and latest_p_img != "":
            contents = contents.replace(prod+"-[YYYYMMDD]V[VERSION]_IMG.zip", latest_p_img)

    # Write out new HTML file.
    move(target_file, target_file + "_OLD")
    with open(target_file, 'w') as f2: 
        f2.write(contents)


def get_latest_product(family, product, product_suffix, product_dir) -> str:
    """Retrieves the name of the most current map product file.

    Args:
        family (string): map family name (e.g. "OSMapaPL" or "OSMapaPLext")
        product (string): map product name (e.g.: "PODSTAWOWA, OGONKI, LIGHT, WARSTWICE, SZLAKI)
        product_suffix (string): map product file name suffix (e.g.: "_IMG.zip" or ".exe")
        product_dir (string): directory where map products are present

    Returns:
        str: map product file name
    """
    command = "ls {product_dir}/{family}-{product}-*{product_suffix} | sort -r | head -1 | xargs -n 1 basename".format(family=family, product=product, product_suffix=product_suffix, product_dir=product_dir)
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
    return result.stdout.rstrip()


if __name__ == "__main__":
    import sys
    import argparse
    
    primary_def_name = "osmapa.www.refresh_index_html()"
    print("Running {primary_def_name} as script...".format(primary_def_name=primary_def_name))
    
    parser = argparse.ArgumentParser(description='Process HTML files of Osmap Garmin.')
    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("-d", "--pdir", help="directory where products are located", required=True)
    requiredNamed.add_argument("-l", "--plist", help='a list of product names (e.g. "FAMILY-PRODUCT" in FAMILY-PRODUCT-[YYYYMMDD]V[VERSION].exe)', required=True)
    requiredNamed.add_argument("-t", "--template", help="source index.html file with placeholder tags ([YYYYMMDD] and [VERSION])", required=True)
    requiredNamed.add_argument("-o", "--output", help="target index.html file to be (over)written after tags have been replaced with values", required=True)
    args = parser.parse_args()

    refresh_index_html(product_dir=args.pdir, product_list=args.plist, template_file=args.template, target_file=args.output)
    
    print("Refreshed {target_file}.".format(args.output))