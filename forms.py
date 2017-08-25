from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, IPAddress
import re

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last Name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Invalid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password.")])
	submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("Please Enter your email address"), Email("Invalid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password")])
	submit = SubmitField("Sign in")
	
class RT_ET_Form(Form):
	Hostname = StringField('Hostname', validators=[DataRequired("You must enter a Hostname")])
	Hostname_Suffix = StringField('Hostname Suffix', validators=[DataRequired("You must enter a Hostname_Suffix")])
	ET_Software_Version = StringField('ET Software Version', validators=[DataRequired("You must enter a ET_Software_Version")])
	Enable_password = StringField('Enable_password', validators=[DataRequired("You must enter a Enable_password")])
	Local_ACS_Server_Primary = StringField('Local ACS Server Primary', validators=[DataRequired("You must enter a Local_ACS_Server_Primary"), IPAddress("This must be an IP address x.x.x.x")])
	Tacacs_Key = StringField('Tacacs Key', validators=[DataRequired("You must enter a Tacacs_Key")])
	Local_ACS_Server_Secondary = StringField('Local ACS Server Secondary', validators=[DataRequired("You must enter a Local_ACS_Server_Secondary"), IPAddress("This must be an IP address x.x.x.x")])
	Local_Admin_Password = StringField('Local Admin Password', validators=[DataRequired("You must enter a Local_Admin_Password")])
	OBX_IPv4_Loopback = StringField('OBX IPv4 Loopback', validators=[DataRequired("You must enter a OBX_IPv4_Loopback"), IPAddress("This must be an IP address x.x.x.x")])
	Nx_ipv4_Loopback = StringField('Nx_ipv4 Loopback', validators=[DataRequired("You must enter a Nx_ipv4_Loopback"), IPAddress("This must be an IP address x.x.x.x")])
	Bgp_ipv4_loopback = StringField('Bgp_ipv4_loopback', validators=[DataRequired("You must enter a Bgp_ipv4_loopback"), IPAddress("This must be an IP address x.x.x.x")])
	Bgp_sendlabel_loopback = StringField('Bgp_sendlabel_loopback', validators=[DataRequired("You must enter a Bgp_sendlabel_loopback"), IPAddress("This must be an IP address x.x.x.x")])
	Bgp_vpnv4_loopback = StringField('Bgp_vpnv4_loopback', validators=[DataRequired("You must enter a Bgp_vpnv4_loopback"), IPAddress("This must be an IP address x.x.x.x")])
	Partner_link_interface = StringField('Partner_link_interface', validators=[DataRequired("You must enter a Partner_link_interface")])
	Partner_link_ipv4addr = StringField('Partner_link_ipv4addr', validators=[DataRequired("You must enter a Partner_link_ipv4addr"), IPAddress("This must be an IP address x.x.x.x")])
	Northbound_a_interface = StringField('Northbound a interface', validators=[DataRequired("You must enter a Northbound_a_interface")])
	Northbound_a_hostname = StringField('Northbound a hostname', validators=[DataRequired("You must enter a Northbound_a_hostname")])
	Northbound_a_ipv4addr = StringField('Northbound a ipv4addr', validators=[DataRequired("You must enter a Northbound_a_ipv4addr"), IPAddress("This must be an IP address x.x.x.x")])
	Northbound_b_interface = StringField('Northbound b interface', validators=[DataRequired("You must enter a Northbound_b_interface")])
	Northbound_b_hostname = StringField('Northbound b hostname', validators=[DataRequired("You must enter a Northbound_b_hostname")])
	Northbound_b_ipv4addr = StringField('Northbound b ipv4addr', validators=[DataRequired("You must enter a Northbound_b_ipv4addr"), IPAddress("This must be an IP address x.x.x.x")])
	Backbone_a_interface = StringField('Backbone a interface', validators=[DataRequired("You must enter a Backbone_a_interface")])
	Backbone_a_peer = StringField('Backbone a peer', validators=[DataRequired("You must enter a Backbone_a_peer")])
	Backbone_a_peer_suffix = StringField('Backbone a peer_suffix', validators=[DataRequired("You must enter a Backbone_a_peer_suffix")])
	Backbone_a_link_circuitid = StringField('Backbone a link_circuitid', validators=[DataRequired("You must enter a Backbone_a_link_circuitid")])
	Backbone_a_ipv4addr = StringField('Backbone a ipv4addr', validators=[DataRequired("You must enter a Backbone_a_ipv4addr"), IPAddress("This must be an IP address x.x.x.x")])
	Oob_switch = StringField('Oob switch', validators=[DataRequired("You must enter a Oob_switch")])
	Oob_switch_interface = StringField('Oob switch interface', validators=[DataRequired("You must enter a Oob_switch_interface")])
	Oob_ipv4addr = StringField('Oob ipv4addr', validators=[DataRequired("You must enter a Oob_ipv4addr"), IPAddress("This must be an IP address x.x.x.x")])
	Lo1000_ipv4addr_encoded = StringField('Lo1000 ipv4addr encoded', validators=[DataRequired("You must enter a Lo1000_ipv4addr_encoded")])
	Backbone_neighbor_bgp_vpnv4_loopback = StringField('Backbone neighbor bgp vpnv4 loopback', validators=[DataRequired("You must enter a Backbone_neighbor_bgp_vpnv4_loopback"), IPAddress("This must be an IP address x.x.x.x")])
	Backbone_a_suffix = StringField('Backbone a suffix', validators=[DataRequired("You must enter a Backbone_a_suffix")])
	Backbone_neighbor_bgp_ipv4_loopback = StringField('Backbone neighbor bgp ipv4 loopback', validators=[DataRequired("You must enter a Backbone_neighbor_bgp_ipv4_loopback"), IPAddress("This must be an IP address x.x.x.x")])
	Oob_switch_ipv4addr = StringField('Oob switch ipv4addr', validators=[DataRequired("You must enter a Oob_switch_ipv4addr"), IPAddress("This must be an IP address x.x.x.x")])
	Oob_switch_ipv4addr_mask = StringField('Oob switch ipv4addr mask', validators=[DataRequired("You must enter a Oob_switch_ipv4addr_mask")])
	Site_id = StringField('Site id', validators=[DataRequired("You must enter a Site_id")])
	Region_id = StringField('Region id', validators=[DataRequired("You must enter a Region_id")])
	Location_description = StringField('Location description', validators=[DataRequired("You must enter a Location_description")])
	submit = SubmitField('Generate')

class testform(Form):
	template_fields = []
	jinja_template = open('./jinja2/rt_alg_to_et_bgp.j2')
	for line in jinja_template:
		for f in re.findall(r'{{\s(.*?)\s}}', line):
			template_fields.append(f)
	for l in template_fields:
		field = str(l).strip("['']")
		setattr(Form, field, StringField(field, validators=[DataRequired()]))
	submit = SubmitField('Generate')

    

