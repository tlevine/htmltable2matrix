

def htmltable2matrix(tablehtml):
  """Takes an lxml tree whose current node is the table of interest"""
  trs=tablehtml.xpath('tr')
  tablematrix=[]
  for tr in trs:
    tablematrix_row=[]
    tds=tr.xpath('td')
    for td in tds:
      #If it has a colspan attribute, repeat that many times
      if 'colspan' in [key.lower() for key in td.attrib.keys()]:
        repeats=int(td.attrib['colspan'])
      else:
        repeats=1

      for r in range(repeats):
        tablematrix_row.append(td.text)
    tablematrix.append(tablematrix_row)
    del(tds)
  return tablematrix