STATE_INFO = {
    "Andhra Pradesh": {
        "code": "S01",
        "modifiable_website_root": "https://ceoaperolls.ap.gov.in/AP_Eroll_2022/Popuppage",
        "suffix_formatted_string": "?partNumber=%s&roll=EnglishMotherRoll&districtName=DIST_%s&acname=13&acnameeng=A%s&acno=%s",
        "captcha_required_on_each_edit": True ,
        "padding": []
    },
    "Arunachal Pradesh": {
        "code": "S02",
        "modifiable_website_root": "http://164.100.149.171/drollwop2023",
        "suffix_formatted_string": "",
        "captcha_required_on_each_edit": False
    },
    "Assam": {
        "code": "S03",
        "modifiable_website_root": "http://103.8.249.227:8080/voterlist/pdfroll/",
        "suffix_formatted_string": "D{dist_no}/A{ac_no}/MotherRoll/S03A{ac_no}P{part_no}.pdf",
        "captcha_required_on_each_edit": False,
        "padding": [],
        "district_map": {
            'BAKSA': '15',
            'BARPETA': '11',
            'BISWANATH': '30',
            'BONGAIGAON': '9',
            'CACHAR': '3',
            'CHARAIDEO': '33',
            'CHIRANG': '8',
            'DARRANG': '16',
            'DHEMAJI': '25',
            'DHUBRI': '6',
            'DIBRUGARH': '26',
            'DIMA HASAO': '4',
            'GOALPARA': '10',
            'GOLAGHAT   ': '21',
            'HAILAKANDI': '2',
            'HOJAI': '31',
            'JORHAT': '22',
            'KAMRUP (METRO)': '13',
            'KAMRUP. ': '12',
            'KARBI ANGLONG ': '5',
            'KARIMGANJ': '1',
            'KOKRAJHAR': '7',
            'LAKHIMPUR': '24',
            'MAJULI': '32',
            'MORIGAON ': '19',
            'NAGAON ': '20',
            'NALBARI': '14',
            'SIVASAGAR': '23',
            'SONITPUR': '18',
            'SOUTH SALMARA MANKACHAR': '29',
            'TINSUKIA': '27',
            'UDALGURI': '17',
            'WEST KARBI ANGLONG': '28'
        }
    },
    "Bihar": {
        "code": "S04",
        "modifiable_website_root": "",
        "suffix_formatted_string": "",
        "captcha_required_on_each_edit": False,
    },
    "Goa": {
        "code": "S05",
        "modifiable_website_root": "https://ceogoa.nic.in/PDF/EROLL/MOTHERROLL/2021/",
        "suffix_formatted_string": "{ac_no}/S05A{ac_no}P{part_no}.pdf",
        "captcha_required_on_each_edit": False,
        "padding": []
    },
    "Gujarat": {
        "code": "S06",
        "modifiable_website_root": "https://erms.gujarat.gov.in/ceo-gujarat/DRAFT2022/",
        "suffix_formatted_string": "{0:03d}/S06A{ac_no}P{part_no}.pdf",
        "captcha_required_on_each_edit": False,
        "paddings": [(0, 3)]
    },
    "Harayana": {
        "code": "S07",
        "modifiable_website_root": "",
        "suffix_formatted_string": "",
        "captcha_required_on_each_edit": False,
    },
    "Himachal Pradesh": {
        "code": "S08",
        "modifiable_website_root": ""
    },
    "Jammu and Kashmir": {
        "code": "S09",
        "modifiable_website_root": ""
    },
    "Karnataka": {
        "code": "S10",
        "modifiable_website_root": "https://ceo.karnataka.gov.in/draftroll_2023/CodeCaputer1.aspx?field1=.%2fKANNADA%2fMR%2fAC069%2fS10A69P5.pdf&field2=69&field3=0005",
        "suffix_formatted_string": "%s/S06A%sP%s.pdf",
        "captcha_required_on_each_edit": False,
        "paddings": [0]
    },
    "Kerala": {
        "code": "S11",
        "modifiable_website_root": ""
    },
    "Madhya Pradesh": {
        "code": "S12",
        "modifiable_website_root": ""
    },
    "Maharashatra": {
        "code": "S13",
        "modifiable_website_root": ""
    },
    "Manipur": {
        "code": "S14",
        "modifiable_website_root": ""
    },
    "Meghalaya": {
        "code": "S15",
        "modifiable_website_root": "https://ceomeghalaya.nic.in/erolls/pdf/english/",
        "suffix_formatted_string": "A{0:03d}/A{0:03d}{0:04d}.pdf",
        "captcha_required_on_each_edit": False,
        "padding": [(0, 3), (1, 3), (2, 4)]
    },
    "Mizoram": {
        "code": "S16",
        "modifiable_website_root": r"https://ceo.mizoram.gov.in/ERollReportWithoutPhoto/S16/13-AIZAWL%20EAST%20I/",
        "suffix_formatted_string": "S16A{ac_no}P{part_no}.pdf",
        "captcha_required_on_each_edit": False,
        "padding": []
    },
    "Nagaland": {
        "code": "S17",
        "modifiable_website_root": ""
    },
    "Odisha": {
        "code": "S18",
        "modifiable_website_root": ""
    },
    "Punjab": {
        "code": "S19",
        "modifiable_website_root": ""
    },
    "Rajasthan": {
        "code": "S20",
        "modifiable_website_root": ""
    },
    "Sikkim": {
        "code": "S21",
        "modifiable_website_root": "https://ceosikkim.nic.in/ElectoralRolls/PDFView?PDFUrl=https://ceosikkim.nic.in/UploadedFiles/ElectoralRollPolling/",
        "suffix_formatted_string": "S21A{ac_no}P%{part_no}.pdf",
        "captcha_required_on_each_edit": False
    },
    "Tamil Nadu": {
        "code": "S22",
        "modifiable_website_root": ""
    },
    "Tripura": {
        "code": "S23",
        "modifiable_website_root": ""
    },
    "Uttar Pradesh": {
        "code": "S24",
        "modifiable_website_root": ""
    },
    "West Bengal": {
        "code": "S25",
        "modifiable_website_root": "https://ceowestbengal.nic.in/DraftRoll?",
        "suffix_formatted_string": "DCID={dist_no}%20&ACID={ac_no}&PSID={part_no}",
        "captcha_required_on_each_edit": False,
        "district_map": {
            "COOCHBEHAR": "1",
            "JALPAIGURI": "2",
            "DARJEELING": "3",
            "UTTAR DINAJPUR": "4",
            "DAKHSIN DINAJPUR": "5",
            "MALDA": "6",
            "MURSHIDABAD": "7",
            "NADIA": "8",
            "NORTH 24 PARGANAS": "9",
            "SOUTH 24 PARGANAS": "10",
            "KOLKATA SOUTH": "11",
            "KOLKATA NORTH": "12",
            "HOWRAH": "14",
            "HOOGHLY": "15",
            "PASCHIM MEDINIPUR": "16",
            "PURBO MEDINIPUR": "17",
            "PURULIA": "18",
            "BANKURA": "19",
            "PURBA BARDHAMAN": "20",
            "BIRBHUM": "21",
            "ALIPURDUAR": "22",
            "KALIMPONG": "23",
            "JHARGRAM": "24",
            "PASCHIM BARDHAMAN": "25"
        }
    },
    "Chhatisgarh": {
        "code": "S26",
        "modifiable_website_root": ""
    },
    "Jharkhand": {
        "code": "S27",
        "modifiable_website_root": "http://164.100.150.3/mrollpdf1/aceng.aspx"
    },
    "Uttarakhand": {
        "code": "S28",
        "modifiable_website_root": ""
    },
    "Telangana": {
        "code": "S29",
        "modifiable_website_root": "https://ceotserms2.telangana.gov.in/ts_erolls/Popuppage.aspx?",
        "suffix_formatted_string": "partNumber=%s&roll=EnglishMotherRoll&districtName=DIST_%s&acname=AC_%s&acnameeng=A%s&acno=%s",
        "captcha_required_on_each_edit": True,
        "paddings": [(1, 2), (2, 3)]
    },
    "Andaman": {
        "code": "U01",
        "modifiable_website_root": ""
    },
    "Chandigarh": {
        "code": "U02",
        "modifiable_website_root": "https://ceochandigarh.gov.in/sites/default/files/polling_files/",
        "suffix_formatted_string": "w001{0:05d}.pdf",
        "captcha_required_on_each_edit": False,
        "paddings": [(0, 4)]
    },
    "Dadra & Nagar Haveli and Daman & Diu": {
        "code": "U03",
        "modifiable_website_root": ""
    },
    "Daman": {
        "code": "U04",
        "modifiable_website_root": ""
    },
    "Delhi": {
        "code": "U05",
        "modifiable_website_root": "https://ceodelhi.gov.in/engdata/",
        "suffix_formatted_string": "AC{ac_no}/U05A{ac_no}P{part_no}.pdf",
        "captcha_required_on_each_edit": False,
        "paddings": []
    },
    "Lakshwadeep": {
        "code": "U06",
        "modifiable_website_root": "https://ceolakshadweep.gov.in/assets/pdf/voterlist/",
        "suffix_formatted_string": "U06A{ac_no}P{part_no}.pdf",
        "captcha_required_on_each_edit": False,
        "paddings": []
    },
    "Puducherry": {
        "code": "U07",
        "modifiable_website_root": ""
    },
}