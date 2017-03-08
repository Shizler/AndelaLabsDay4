def find_missing(alist,my_list):
  len1=len(my_list)
  len2=len(alist)
  
  if len1==0 or len2==0:
      return 0
  if len1==len2:
      return 0
  else:
      return list(set(alist).symmetric_difference(set(my_list)))[0]