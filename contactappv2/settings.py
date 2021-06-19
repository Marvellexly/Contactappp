class Settings:

	def __init__(self):

		#App Conf
		self.title = "Apotek Sahabat"

		#Window Conf
		base = 50
		ratio = (16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+500+500"


		#Image Conf
		self.logo = 'img/Apotek.jpg'

		#Data Dummy
		self.contacts = [
		{
			"081123456789" : {
				"f_name" : "Ali",
				"l_name" : "Umar",
				"address" : "Pasar Kuto Selatan",
				"email" : "AliUmar@gmail.com",
				"Obat" : "Paracetamol",
				"Exp_Date" : "25 Okt 2030"
			} 
		},
		{
			"081123456789" : {
				"f_name" : "Muhammad",
				"l_name" : "Satria",
				"address" : "Km 12",
				"email" : "AnasAzhar@gmail.com",
				"Obat" : "Aspirin",
				"Exp_Date" : "13 Jan 2028"
			}
		},
		{
			"082123456789" : {
				"f_name" : "Bambang",
				"l_name" : "Triadmodjo",
				"address" : "Sekip",
				"email" : "BambangTriadmodjo@gmail.com",
				"Obat" : "Bodrex",
				"Exp_Date" : "27 Mei 2032"

			}
		},
		{
			"083123456789" : {
				"f_name" : "Cindy",
				"l_name" : "Situmorang",
				"address" : "Plaju",
				"email" : "CindySitumorang@gmail.com",
				"Obat" : "Vaksin Covid 19",
				"Exp_Date" : "14 Juli 2040"


			}
		},
		{
			"085123456789" : {
				"f_name" : "Dono",
				"l_name" : "Kasino",
				"address" : "Cinde",
				"email" : "DonoKasino@gmail.com",
				"Obat" : "Sakatonik ABC",
				"Exp_Date" : "30 Des 2039"
			}
		}
		]
		