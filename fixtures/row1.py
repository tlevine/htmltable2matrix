days="""<form>
<table>
<tr>
<td align="center" style="color:#ff0000"><img src="/apps/SSAdmin/views/images/downArrow.gif"></td>
<td style="color:#ff0000; font-size: 14px;">Select Day<br>of Travel</td>
</tr>
</table><select name="selFrequency" onchange="window.location='/coachSS/index.asp?action=RouteReload&amp;order=&amp;sitePageName=%2Fshortline%2Fss.details.asp&amp;dayFilter='+this.value;"><option value="">
    			Show All
    		</option>
<option value="">Show All</option>
<option value="All">Daily</option>
<option value="Weekdays">Weekdays</option>
<option value="Mo">Monday</option>
<option value="Tu">Tuesday</option>
<option value="We">Wednesday</option>
<option value="Th">Thursday</option>
<option value="Fr">Friday</option>
<option value="Sa">Saturday</option>
<option value="Su">Sunday</option></select></form>
    		&nbsp;
    	"""

fromstop1="""<table cellspacing="0" cellpadding="0" border="0"><tr><td align="left" valign="top"><!--mp_trans_disable_start--><img src="/apps/ssadmin/actions/RenderStopName_ah.asp?title=Cornell%2C%20North%20Campus%2C%20CC%20Lot" alt="Cornell, North Campus, CC Lot" title="Cornell, North Campus, CC Lot"><!--mp_trans_disable_end--></td></tr></table>"""

fromstop2="""<table cellspacing="0" cellpadding="0" border="0"><tr><td align="left" valign="top"><!--mp_trans_disable_start--><img src="/apps/ssadmin/actions/RenderStopName_ah.asp?title=Cornell%2C%20West%20Campus%2C%20Baker's%20Flagpole" alt="Cornell, West Campus, Baker's Flagpole" title="Cornell, West Campus, Baker's Flagpole"><!--mp_trans_disable_end--></td>\r\n</tr></table>"""

fromstop3="""<table cellspacing="0" cellpadding="0" border="0"><tr><td align="left" valign="top"><!--mp_trans_disable_start--><img src="/apps/ssadmin/actions/RenderStopName_ah.asp?title=Cornell%2C%20Theater%20Arts%20Ctr." alt="Cornell, Theater Arts Ctr." title="Cornell, Theater Arts Ctr."><!--mp_trans_disable_end--></td>\r\n</tr></table>"""

fromstop4="""<table cellspacing="0" cellpadding="0" border="0"><tr><td align="left" valign="top"><!--mp_trans_disable_start--><img src="/apps/ssadmin/actions/RenderStopName_ah.asp?title=State%20Street%2C%20Terminal" alt="State Street, Terminal" title="State Street, Terminal"><!--mp_trans_disable_end--></td>\r\n</tr></table>"""
arrow=""

tostop="""<table cellspacing="0" cellpadding="0" border="0"><tr><td align="left" valign="top"><!--mp_trans_disable_start--><img src="/apps/ssadmin/actions/RenderStopName_ah.asp?title=Port%20Authority%20Bus%20Terminal" alt="Port Authority Bus Terminal" title="Port Authority Bus Terminal"><!--mp_trans_disable_end--></td>\r\n</tr></table>"""

route="""<img src="/apps/SSAdmin/views/images/routeTrip.jpg" alt="Route/Trip" title="Route/Trip" width="20" height="110">"""
