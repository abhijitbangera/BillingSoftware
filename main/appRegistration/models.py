from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class memberDetails(models.Model):
	memberName=models.CharField('Full Name', max_length=100)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	memberGender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES)
	memberCity=models.CharField('City',max_length=100)
	memberAddress=models.TextField('Address', blank=True)
	memberPincode=models.IntegerField('Pincode', max_length=9,blank=True)
	memberContactNumber=models.IntegerField('Contact Number',max_length=14)
	memberEmergencyNumber=models.IntegerField('Emergency Contact Number', max_length=14,blank=True)
	memberEmail=models.EmailField('Email ID', max_length=100)
	memberRegistrationDate=models.DateTimeField('Registration Date')
	memberNumber=models.IntegerField(max_length=9,primary_key=True, null=False)
	memberStatus=models.BooleanField('Status', default=True)
	memberPlan=models.CharField('Subscription Plan', max_length=100)
	memberPlanActivationDate=models.DateTimeField('Subscription Activation Date')
	memberPlandExpiryDate=models.DateTimeField('Subscription Expiry Date')
	memberGymNumber=models.ForeignKey('gymDetails')

	def __str__(self):
		return str(self.memberNumber)

class gymDetails(models.Model):
	COUNTRIES = (
			    ('AD', 'Andorra'),
			    ('AE', 'United Arab Emirates'),
			    ('AF', 'Afghanistan'),
			    ('AG', 'Antigua & Barbuda'),
			    ('AI', 'Anguilla'),
			    ('AL', 'Albania'),
			    ('AM', 'Armenia'),
			    ('AN', 'Netherlands Antilles'),
			    ('AO', 'Angola'),
			    ('AQ', 'Antarctica'),
			    ('AR', 'Argentina'),
			    ('AS', 'American Samoa'),
			    ('AT', 'Austria'),
			    ('AU', 'Australia'),
			    ('AW', 'Aruba'),
			    ('AZ', 'Azerbaijan'),
			    ('BA', 'Bosnia and Herzegovina'),
			    ('BB', 'Barbados'),
			    ('BD', 'Bangladesh'),
			    ('BE', 'Belgium'),
			    ('BF', 'Burkina Faso'),
			    ('BG', 'Bulgaria'),
			    ('BH', 'Bahrain'),
			    ('BI', 'Burundi'),
			    ('BJ', 'Benin'),
			    ('BM', 'Bermuda'),
			    ('BN', 'Brunei Darussalam'),
			    ('BO', 'Bolivia'),
			    ('BR', 'Brazil'),
			    ('BS', 'Bahama'),
			    ('BT', 'Bhutan'),
			    ('BV', 'Bouvet Island'),
			    ('BW', 'Botswana'),
			    ('BY', 'Belarus'),
			    ('BZ', 'Belize'),
			    ('CA', 'Canada'),
			    ('CC', 'Cocos (Keeling) Islands'),
			    ('CF', 'Central African Republic'),
			    ('CG', 'Congo'),
			    ('CH', 'Switzerland'),
			    ('CI', 'Ivory Coast'),
			    ('CK', 'Cook Iislands'),
			    ('CL', 'Chile'),
			    ('CM', 'Cameroon'),
			    ('CN', 'China'),
			    ('CO', 'Colombia'),
			    ('CR', 'Costa Rica'),
			    ('CU', 'Cuba'),
			    ('CV', 'Cape Verde'),
			    ('CX', 'Christmas Island'),
			    ('CY', 'Cyprus'),
			    ('CZ', 'Czech Republic'),
			    ('DE', 'Germany'),
			    ('DJ', 'Djibouti'),
			    ('DK', 'Denmark'),
			    ('DM', 'Dominica'),
			    ('DO', 'Dominican Republic'),
			    ('DZ', 'Algeria'),
			    ('EC', 'Ecuador'),
			    ('EE', 'Estonia'),
			    ('EG', 'Egypt'),
			    ('EH', 'Western Sahara'),
			    ('ER', 'Eritrea'),
			    ('ES', 'Spain'),
			    ('ET', 'Ethiopia'),
			    ('FI', 'Finland'),
			    ('FJ', 'Fiji'),
			    ('FK', 'Falkland Islands (Malvinas)'),
			    ('FM', 'Micronesia'),
			    ('FO', 'Faroe Islands'),
			    ('FR', 'France'),
			    ('FX', 'France, Metropolitan'),
			    ('GA', 'Gabon'),
			    ('GB', 'United Kingdom (Great Britain)'),
			    ('GD', 'Grenada'),
			    ('GE', 'Georgia'),
			    ('GF', 'French Guiana'),
			    ('GH', 'Ghana'),
			    ('GI', 'Gibraltar'),
			    ('GL', 'Greenland'),
			    ('GM', 'Gambia'),
			    ('GN', 'Guinea'),
			    ('GP', 'Guadeloupe'),
			    ('GQ', 'Equatorial Guinea'),
			    ('GR', 'Greece'),
			    ('GS', 'South Georgia and the South Sandwich Islands'),
			    ('GT', 'Guatemala'),
			    ('GU', 'Guam'),
			    ('GW', 'Guinea-Bissau'),
			    ('GY', 'Guyana'),
			    ('HK', 'Hong Kong'),
			    ('HM', 'Heard & McDonald Islands'),
			    ('HN', 'Honduras'),
			    ('HR', 'Croatia'),
			    ('HT', 'Haiti'),
			    ('HU', 'Hungary'),
			    ('ID', 'Indonesia'),
			    ('IE', 'Ireland'),
			    ('IL', 'Israel'),
			    ('IN', 'India'),
			    ('IO', 'British Indian Ocean Territory'),
			    ('IQ', 'Iraq'),
			    ('IR', 'Islamic Republic of Iran'),
			    ('IS', 'Iceland'),
			    ('IT', 'Italy'),
			    ('JM', 'Jamaica'),
			    ('JO', 'Jordan'),
			    ('JP', 'Japan'),
			    ('KE', 'Kenya'),
			    ('KG', 'Kyrgyzstan'),
			    ('KH', 'Cambodia'),
			    ('KI', 'Kiribati'),
			    ('KM', 'Comoros'),
			    ('KN', 'St. Kitts and Nevis'),
			    ('KP', 'Korea, Democratic People\'s Republic of'),
			    ('KR', 'Korea, Republic of'),
			    ('KW', 'Kuwait'),
			    ('KY', 'Cayman Islands'),
			    ('KZ', 'Kazakhstan'),
			    ('LA', 'Lao People\'s Democratic Republic'),
			    ('LB', 'Lebanon'),
			    ('LC', 'Saint Lucia'),
			    ('LI', 'Liechtenstein'),
			    ('LK', 'Sri Lanka'),
			    ('LR', 'Liberia'),
			    ('LS', 'Lesotho'),
			    ('LT', 'Lithuania'),
			    ('LU', 'Luxembourg'),
			    ('LV', 'Latvia'),
			    ('LY', 'Libyan Arab Jamahiriya'),
			    ('MA', 'Morocco'),
			    ('MC', 'Monaco'),
			    ('MD', 'Moldova, Republic of'),
			    ('MG', 'Madagascar'),
			    ('MH', 'Marshall Islands'),
			    ('ML', 'Mali'),
			    ('MN', 'Mongolia'),
			    ('MM', 'Myanmar'),
			    ('MO', 'Macau'),
			    ('MP', 'Northern Mariana Islands'),
			    ('MQ', 'Martinique'),
			    ('MR', 'Mauritania'),
			    ('MS', 'Monserrat'),
			    ('MT', 'Malta'),
			    ('MU', 'Mauritius'),
			    ('MV', 'Maldives'),
			    ('MW', 'Malawi'),
			    ('MX', 'Mexico'),
			    ('MY', 'Malaysia'),
			    ('MZ', 'Mozambique'),
			    ('NA', 'Namibia'),
			    ('NC', 'New Caledonia'),
			    ('NE', 'Niger'),
			    ('NF', 'Norfolk Island'),
			    ('NG', 'Nigeria'),
			    ('NI', 'Nicaragua'),
			    ('NL', 'Netherlands'),
			    ('NO', 'Norway'),
			    ('NP', 'Nepal'),
			    ('NR', 'Nauru'),
			    ('NU', 'Niue'),
			    ('NZ', 'New Zealand'),
			    ('OM', 'Oman'),
			    ('PA', 'Panama'),
			    ('PE', 'Peru'),
			    ('PF', 'French Polynesia'),
			    ('PG', 'Papua New Guinea'),
			    ('PH', 'Philippines'),
			    ('PK', 'Pakistan'),
			    ('PL', 'Poland'),
			    ('PM', 'St. Pierre & Miquelon'),
			    ('PN', 'Pitcairn'),
			    ('PR', 'Puerto Rico'),
			    ('PT', 'Portugal'),
			    ('PW', 'Palau'),
			    ('PY', 'Paraguay'),
			    ('QA', 'Qatar'),
			    ('RE', 'Reunion'),
			    ('RO', 'Romania'),
			    ('RU', 'Russian Federation'),
			    ('RW', 'Rwanda'),
			    ('SA', 'Saudi Arabia'),
			    ('SB', 'Solomon Islands'),
			    ('SC', 'Seychelles'),
			    ('SD', 'Sudan'),
			    ('SE', 'Sweden'),
			    ('SG', 'Singapore'),
			    ('SH', 'St. Helena'),
			    ('SI', 'Slovenia'),
			    ('SJ', 'Svalbard & Jan Mayen Islands'),
			    ('SK', 'Slovakia'),
			    ('SL', 'Sierra Leone'),
			    ('SM', 'San Marino'),
			    ('SN', 'Senegal'),
			    ('SO', 'Somalia'),
			    ('SR', 'Suriname'),
			    ('ST', 'Sao Tome & Principe'),
			    ('SV', 'El Salvador'),
			    ('SY', 'Syrian Arab Republic'),
			    ('SZ', 'Swaziland'),
			    ('TC', 'Turks & Caicos Islands'),
			    ('TD', 'Chad'),
			    ('TF', 'French Southern Territories'),
			    ('TG', 'Togo'),
			    ('TH', 'Thailand'),
			    ('TJ', 'Tajikistan'),
			    ('TK', 'Tokelau'),
			    ('TM', 'Turkmenistan'),
			    ('TN', 'Tunisia'),
			    ('TO', 'Tonga'),
			    ('TP', 'East Timor'),
			    ('TR', 'Turkey'),
			    ('TT', 'Trinidad & Tobago'),
			    ('TV', 'Tuvalu'),
			    ('TW', 'Taiwan, Province of China'),
			    ('TZ', 'Tanzania, United Republic of'),
			    ('UA', 'Ukraine'),
			    ('UG', 'Uganda'),
			    ('UM', 'United States Minor Outlying Islands'),
			    ('US', 'United States of America'),
			    ('UY', 'Uruguay'),
			    ('UZ', 'Uzbekistan'),
			    ('VA', 'Vatican City State (Holy See)'),
			    ('VC', 'St. Vincent & the Grenadines'),
			    ('VE', 'Venezuela'),
			    ('VG', 'British Virgin Islands'),
			    ('VI', 'United States Virgin Islands'),
			    ('VN', 'Viet Nam'),
			    ('VU', 'Vanuatu'),
			    ('WF', 'Wallis & Futuna Islands'),
			    ('WS', 'Samoa'),
			    ('YE', 'Yemen'),
			    ('YT', 'Mayotte'),
			    ('YU', 'Yugoslavia'),
			    ('ZA', 'South Africa'),
			    ('ZM', 'Zambia'),
			    ('ZR', 'Zaire'),
			    ('ZW', 'Zimbabwe'),
			    ('ZZ', 'Others'),
				)
	gymName=models.CharField('Business Name',max_length=100, )
	gymCity=models.CharField('City',max_length=100)
	gymAddress=models.TextField('Address')
	gymPincode=models.IntegerField('Pincode',max_length=9)
	gymCountry=models.CharField('Country',max_length=100,choices=COUNTRIES)
	gymRegistrationDate=models.DateTimeField('Registration Date')
	gymNumber=models.IntegerField(max_length=9,primary_key=True, null=False)
	BusinessType = (('gym', 'Gym'),('yoga', 'Yoga'),)
	gymType=models.CharField('Category',max_length=100,choices=BusinessType)
	gymImage=models.ImageField(upload_to = 'images/', default = 'images/img.jpg')
	gymUser=models.ForeignKey(User, unique=True)

	def __str__(self):
		return str(self.gymNumber)

class gymPlans(models.Model):
	planName=models.CharField('Plan Name',max_length=100)
	planDuration=models.IntegerField('Duration (in days)', default=30, max_length=4,blank=False, null=False)
	planPrice=models.IntegerField('Price/Amount', max_length=9,blank=False, null=False)
	planDescription=models.CharField('Brief Description', max_length=300,blank=True, null=True)
	planGymNumber=models.ForeignKey('gymDetails')
	planStatus=models.BooleanField('Plan Active', default=True)

	def __str__(self):
		return str(self.planName+self.planGymNumber)


class staffDetails(models.Model):
	staffName=models.CharField('Full Name',max_length=100)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	staffGender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES)
	staffCity=models.CharField('City', max_length=100)
	staffAddress=models.TextField('Address', blank=True)
	staffPincode=models.IntegerField('Pincode', max_length=9,blank=True)
	staffContactNumber=models.IntegerField('Contact Number',max_length=14)
	staffEmergencyNumber=models.IntegerField('Emergency Contact Number', max_length=14,blank=True)
	staffEmail=models.EmailField('Email', max_length=100)
	staffRegistrationDate=models.DateTimeField('Registration Date')
	staffNumber=models.IntegerField(max_length=9,primary_key=True, null=False)
	staffStatus=models.BooleanField(default=True)
	staffGymNumber=models.ForeignKey('gymDetails')

	def __str__(self):
		return str(self.staffNumber)