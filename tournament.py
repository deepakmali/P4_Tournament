#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection
    and the cursor"""
    connection = psycopg2.connect("dbname=tournament")
    cursor = connection.cursor()
    return connection, cursor


def disconnect(connection, cursor):
    cursor.close()
    connection.close()


def deleteMatches():
    """Remove all the match records from the database."""
    connection, cursr = connect()
    query = "truncate matches;"
    cursr.execute(query)
    # cursr.execute("update players set wins=0, matches_played=0;")
    connection.commit()
    disconnect(connection, cursr)


def deletePlayers():
    """Remove all the player records from the database."""
    connection, cursr = connect()
    query = "truncate players cascade;"
    cursr.execute(query)
    connection.commit()
    disconnect(connection, cursr)


def countPlayers():
    """Returns the number of players currently registered."""
    connection, cursr = connect()
    query = "select count(*) from players;"
    cursr.execute(query)
    total_players = int(cursr.fetchone()[0])
    disconnect(connection, cursr)
    return total_players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    player_name = bleach.clean(name)
    connection, cursr = connect()
    query = "insert into players(name) values(%s);"
    params = (player_name,)
    cursr.execute(query, params)
    connection.commit()
    disconnect(connection, cursr)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection, cursr = connect()
    query = """select a.id, a.name, (select count(*) from matches where
                winner = a.id) as won,
                (select count(*) from matches
                where winner = a.id or loser = a.id) as matches
                from players a order by won desc ;"""
    cursr.execute(query)
    playerStandings = cursr.fetchall()
    disconnect(connection, cursr)
    return playerStandings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connection, cursr = connect()
    winner_player = bleach.clean(winner)
    loser_player = bleach.clean(loser)
    query = "insert into matches(winner, loser) values(%s, %s) ;"
    params = (winner_player, loser_player)
    cursr.execute(query, params)
    connection.commit()
    disconnect(connection, cursr)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    participants = playerStandings()
    pairings = []
    for i in range(0, len(participants), 2):
        pairings.append((participants[i][0], participants[i][1],
                         participants[i+1][0], participants[i+1][1]))

    return pairings
