user_prompt = """
Exctract information from the following email. there is the glossary about shipment: PU: pickup point, DEL: delivery point, 
            Origin: pickup point, Destination: delivery point, FTL: full truck load, TL: truck load.
            There could be different equipment types, for example Dry, 53ft dry van, Frozen, Reefer.
            If there is no explicit equipment type return Dry. If equipment type is Frozen return Reefer.
            If there is no ZIP code of pickup or delivery point, you should find and return the proper one you know for that city and state, do not miss zip.
"""
