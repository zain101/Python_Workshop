from ConfigParser import ConfigParser

def read_db_config(filename = "config.ini", section = 'mysql'):
    """ Read database configuration file and return a dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of database parameters
    """

    #  create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename);

    db = {}
    if parser.has_section(section):
	
        items = parser.items(section)  #retuen list of tuples
	print items
        for item in items:
            db[item[0]] = item[1]        #converting them to dictionary
    else:
        print "%s not found in %s file " % (section, filename)

    return db;



if __name__ == '__main__':
    db  = read_db_config()
    print "Values: "
    for entry in db:
        print entry, ": ", db[entry]
