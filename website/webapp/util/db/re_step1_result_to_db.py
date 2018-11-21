from webapp.models import *
import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: python ... [origin_iaa_result] [google_iaa_result]", file=sys.stderr)
    exit(1)

origin_iaa_result = sys.argv[1]
google_iaa_result = sys.argv[2]

google_df = pd.read_csv(google_iaa_result, engine="python")
origin_df = pd.read_csv(origin_iaa_result, engine="python")

origin_df.info()
google_df.info()

for idx, row in google_df.iterrows():
    r = ReStep1Results.objects.create(claim_id=row["claim"], perspective_id=row["perspective"], vote_support=row["sup"],
                                  vote_leaning_support=row["lsup"], vote_leaning_undermine=row["lund"],
                                  vote_undermine=row["und"], vote_not_valid=row["not_valid"], p_i_5=row["P_i_5_labels"],
                                  p_i_3=row["P_i_3_labels"])
    r.save()

for idx, row in origin_df.iterrows():
    cid = PerspectiveRelation.objects.get(author=PerspectiveRelation.GOLD, perspective_id=row.perspective).claim_id
    r = ReStep1Results.objects.create(claim_id=cid, perspective_id=row["perspective"], vote_support=row["sup"],
                                  vote_leaning_support=row["lsup"], vote_leaning_undermine=row["lund"],
                                  vote_undermine=row["und"], vote_not_valid=row["not_valid"], p_i_5=row["P_i_5_labels"],
                                  p_i_3=row["P_i_3_labels"])
    r.save()