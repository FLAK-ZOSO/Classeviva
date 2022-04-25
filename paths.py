# URLs
login_url = "https://web.spaggiari.eu/home/app/default/login.php"
main_page_url = "https://web.spaggiari.eu/home/app/default/menu_webinfoschool_studenti.php"
valutazioni_note_url = "https://web.spaggiari.eu/cvv/app/default/genitori_note.php"
valutazioni_voti_url = "https://web.spaggiari.eu/cvv/app/default/genitori_voti.php"
note_url = "https://web.spaggiari.eu/fml/app/default/gioprof_note_studente.php"
registro_url = "https://web.spaggiari.eu/fml/app/default/regclasse.php"
registro_data_url = "https://web.spaggiari.eu/fml/app/default/regclasse.php?data_start={}"

# xPaths for login
code_input = "/html/body/div/main/div[1]/div/div/form/div[1]/div[1]/input"
password_input = "/html/body/div/main/div[1]/div/div/form/div[1]/div[2]/input"
login_button = "/html/body/div/main/div[1]/div/div/form/button"

# xPaths for main page
schoolpass_div = "/html/body/div[4]/table/tbody/tr[5]/td[3]/a/div/div"

# xPaths for valutazioni
subjects_tds = "/html/body/div[4]/div[1]/table/tbody/tr/td[@class='registro redtext open_sans_condensed_bold font_size_20']"
trs = "/html/body/div[4]/div[1]/table/tbody/tr"
marks = "/html/body/div[4]/div/div/div[1]/div[2]/table/tbody/tr/td/div/p[@class='double s_reg_testo cella_trattino']"
all_marks = "/html/body/div[4]/div/div/div[1]/div[1]/button[1]"
written_marks = "/html/body/div[4]/div/div/div[1]/div[1]/button[2]"
oral_marks = "/html/body/div[4]/div/div/div[1]/div[1]/button[3]"
practical_marks = "/html/body/div[4]/div/div/div[1]/div[1]/button[4]"

# xPaths for note
note_option = "/html/body/div[4]/div[1]/div/form/select/option[{}]"
pages_input = "/html/body/div[4]/div[1]/div/form/input"
next_img = "/html/body/div[4]/div[1]/div/form/img[3]"
last_img = "/html/body/div[4]/div[1]/div/form/img[4]"
nota_trs = "/html/body/div[4]/div[1]/table[3]/tbody/tr"
order_tr = "/html/body/div[4]/div[1]/table[3]/thead/tr"

# xPaths for registro
data_a = "/html/body/div[4]/div[1]/table[1]/tbody/tr[8]/td/span[4]/a"
status_p = "/html/body/div[4]/div[1]/form/table/tbody/tr[2]/td[7]/a/div/p[1]"