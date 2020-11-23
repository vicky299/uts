def main():
    BMI_intro()



def mbi_intro():
    print("ayo ! \n")

get_height = float(input("masukkan tinggi badan anda dalam cm:"))
get_weight = float(input("masukkan berat badan anda dalam kg:"))
body_mass_index= (get_weight/((get_height/100)**2))

if body_mass_index < 18 :
    print("status berat badan KURUS")
elif body_mass_index >=18 and body_mass_index < 23 :
    print("status berat badan IDEAL")
elif body_mass_index >=23 and body_mass_index < 27 :
    print("status berat badan GEMUK")
elif body_mass_index >= 27 and body_mass_index < 35 :
    print("status berat badan OBESITAS")
elif body_mass_index >= 35 :
    print("status berat badan OBESITAS MORBID")


