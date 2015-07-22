SANITY CHECK DRAFT

sanity check will perform the following:

    1) renew token
    2) create an asset
    3) patch an asset
    4) get an asset
    5) delete asset
    6) create project
    7) get entitlements
    8) get project
    9) delete project


    usages==============================================================================

        srenew.py - renew token (patch request) every 9 minutes
        stest.py - sanity check draft
        sdelassets.py - draft for deleting assets (to be added to sanity check/stest.py)


When verified working, these will be put as tasks on locustfile.py
