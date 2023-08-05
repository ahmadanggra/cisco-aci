#!/usr/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'unique': self.unique
        }
    
    '''
    Move existing list of dict into new list of dict with reduced dict keys, afteward if any duplicated dict found in the list.
    remove it from the list.

    For example following data
    data = [
    {'tenant': 'Heroes_Evils','contract': 'web_http_ct','scope': 'context','subject':'web_http_subj','filter':'http_filt'},
    {'tenant': 'Heroes_Evils','contract': 'web_http_ct','scope': 'context','subject':'web_http_subj','filter':'https_filt'},
    {'tenant': 'Heroes_Evils','contract': 'db_ct','scope': 'context','subject':'db_subj','filter':'db_filt'},
    {'tenant': 'Heroes_Evils','contract': 'ssh_ct','scope': 'context','subject':'ssh_subj','filter':'ssh_filt'},
    {'tenant': 'Heroes_Evils','contract': 'proxy_ct','scope': 'context','subject':'proxy_subj','filter':'80_filt'},
    {'tenant': 'Heroes_Evils','contract': 'proxy_ct','scope': 'context','subject':'proxy_subj','filter':'8080_filt'},
    ]
    
    will become following data, if the unique function called by: for example unique(data, 'tenant', 'contract', 'scope')
    data_new = [
    {'tenant': 'Heroes_Evils', 'contract': 'web_http_ct', 'scope': 'context'}
    {'tenant': 'Heroes_Evils', 'contract': 'db_ct', 'scope': 'context'}
    {'tenant': 'Heroes_Evils', 'contract': 'ssh_ct', 'scope': 'context'}
    {'tenant': 'Heroes_Evils', 'contract': 'proxy_ct', 'scope': 'context'}
    ]
    ''' 
    def unique(self, items: list, *argv):
        temp = list()
        temp_dict = dict()
        remove_dup = list()
      
        # initialize temp_dict
        for arg in argv:
            temp_dict[arg] = ""
        
        # move data from items to temp with supplied keys
        for i in items:
            for j in temp_dict.keys():
                      temp_dict[j] = i[j]
            temp.append(temp_dict.copy())
        
        # eliminate duplicate on dict
        checker = True
        for i in temp:
            # we must populate list first because we can not loop an empty list
            if len(remove_dup) == 0:
                 remove_dup.append(i)
            for j in remove_dup:
                if i == j:
                    checker = True
                else:
                    checker = False
            if checker == False:
                 remove_dup.append(i)
                
        return remove_dup

