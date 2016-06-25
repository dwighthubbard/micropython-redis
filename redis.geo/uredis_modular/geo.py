from .client import Client


class Geo(Client):
    def geoadd(self, *args):
        """
        Add one or more geospatial items in the geospatial index represented using a sorted set

        Parameters
        ----------
        *args
            key longitude latitude member [longitude latitude member ...]

        Returns
        -------
        int
            The number of elements added to the sorted set, not including elements already existing for which the
            score was updated.
        """
        return self.execute_command('GEOADD', *args)

    def geohash(self, *args):
        """
        Members of a geospatial index as geohash strings

        Parameters
        ----------
        *args
            key member [member ...]

        Returns
        -------
        dict
            Returns members of a geospatial index as standard geohash strings
        """
        return self.execute_command('GEOHASH', *args)

    def geopos(self, *args):
        """
        Return longitude and latitude of members of a geospatial index

        Parameters
        ----------
        *args
            key member [key member ...]

        Returns
        -------
        dict
            Returns members of a geospatial index as standard geohash strings
        """
        return self.execute_command('GEOPOS', *args)

    def geodist(self, *args):
        """
        Returns the distance between two members of a geospatial index

        Parameters
        ----------
        *args
            key member1 member2 [unit]
        Returns
        -------
        """
        return self.execute_command('GEODIST', *args)

    def georadius(self, *args):
        """
        Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a point

        Parameters
        ----------
        *args
            key longitude latitude radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]

        Returns
        -------
        """
        return self.execute_command('GEORADIUS', *args)

    def georadiusbymember(self, *args):
        """
        Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a member

        Parameters
        ----------
        *args
            key member radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]

        Returns
        -------
        """
        return self.execute_command('GEORADIUSBYMEMBER', *args)
