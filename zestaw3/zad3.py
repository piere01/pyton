pdk={"cukier": "kg","jajka": "sztuki","mleko":"litry","maka": "kg","olej":"litry","pomarancze": "sztuki"}
print(pdk)
pdk2={key for key in pdk if pdk[key]=="sztuki"}
print(pdk2)