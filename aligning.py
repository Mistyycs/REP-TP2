import requests

def main():
    answer_asso_urls = [
        "https://raw.githubusercontent.com/Mistyycs/REP-TP2/main/answer_associativity.txt",
        "https://raw.githubusercontent.com/Matys53/REP_TP/master/answer_associativity.txt",
        "https://raw.githubusercontent.com/PaulineRoches/REP_popo_sos/main/answer_associativity.txt",
        #"https://raw.githubusercontent.com/l55I1/REP/main/results.txt",
        "https://raw.githubusercontent.com/matth1446/rep_mh_vvk/main/answer_associativity.txt",
        "https://raw.githubusercontent.com/AntoineMarchalDombrat/REP_Antoine_Jean/main/answer_associativity.txt",
        "https://raw.githubusercontent.com/alpjakop/REP/main/answer_associativity.txt",
        "https://raw.githubusercontent.com/Kaeios/assoc-REP/master/answer_associativity.txt",
        "https://raw.githubusercontent.com/Dyskal/repro/main/answer_associativity.txt"
    ]

    resultats = []
    for i in range(len(answer_asso_urls)-1):
        response = requests.get(answer_asso_urls[i])
        if response.status_code == 200:
            with open('answer_asso.txt', 'wb') as file:
                file.write(response.content)
            print("Fichier téléchargé avec succès.")

            with open('answer_asso.txt', 'r', encoding='utf-8') as file:
                contenu = file.read()  
                resultats.append(contenu)
                resultats[i] = resultats[i][:-1]
        else:
            print(f"Erreur lors du téléchargement : {response.status_code} de l'url + {answer_asso_urls [i]}")
        
    print(resultats)
main()