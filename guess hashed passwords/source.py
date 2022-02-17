import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    
    # generating our hash list
    hashes_dictionary = {}
    for i in range(1000,10000):
        result = hashlib.sha256(str(i).encode())
        hashes_dictionary[result.hexdigest()] = i

    # searching for each hash from input file name and writing the found code in output file name
    fin = open(input_file_name, "r")
    fout = open(output_file_name, "a")
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    # reading the information of each user:
    for each_user in reader:
        user_name = each_user[0]
        user_hash = each_user[1]
        
        # start searching for our passcode:
        for hash, number in hashes_dictionary.items():
            if (hash == user_hash):
                print(f"{user_name},{number}")
                # writing the result in output:
                writer.writerow([user_name, number])
    fin.close()
    fout.close()
    
hash_password_hack("hashed.csv", "visible_password.csv")
