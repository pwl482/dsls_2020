"""
Base codes for Agent and its internal state
"""

from enum import Enum
import uuid


class Status(Enum):
    """
    Agent status, following the SIR model
    """
    Susceptible = 's'
    Infected = 'i'
    Recovered_Immune = 'c'
    Death = 'm'


class InfectionSeverity(Enum):
    """
    The Severity of the Infected agents
    """
    Asymptomatic = 'a'
    Exposed = 'e'
    Infectious = 'i'
    Hospitalization = 'h'
    Severe = 'g'


class AgentType(Enum):
    """
    The type of the agent, or the node at the Graph
    """
    Person = 'p'
    Business = 'b'
    House = 'h'
    Government = 'g'
    Healthcare = 'c'


class Agent(object):
    """
    The container of Agent's attributes and status
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', int(uuid.uuid4()))
        self.x = kwargs.get('x', 0)
        """The horizontal position of the agent in the shared environment"""
        self.y = kwargs.get('y', 0)
        """The vertical position of the agent in the shared environment"""
        self.status = kwargs.get('status', Status.Susceptible)
        """The health status of the agent"""
        self.infected_status = kwargs.get('infected_status', InfectionSeverity.Asymptomatic)
        """The infection severity of the agent"""
        self.infected_time = kwargs.get('infected_time', 0)
        """The time (in days) after the infection"""
        # incubation period
        self.exposed_time = kwargs.get('exposed_time', 0)
        '''The time time a person has been exposed to the virus'''
        self.age = kwargs.get('age', 0)
        """The age (in years) of the agent"""
        self.social_stratum = kwargs.get('social_stratum', 0)
        """The social stratum (or their quintile in wealth distribution) of the agent"""
        self.wealth = kwargs.get('wealth', 0.0)
        """The current wealth of the agent"""
        self.type = AgentType.Person
        """The type of the agent"""
        self.environment = kwargs.get('environment', None)
        self.number_infected = 0
        """The number of agents infected by this agent"""
        self.pre_shopping_position = (self.x, self.y)
        """position before going to a shop"""
        self.days_without_shopping = kwargs.get('days_without_shopping', 0)
        """days without shopping"""
        self.is_shopping = False
        """flag for shopping"""

    def get_description(self):
        """
        Get a simplified description of the agent health status

        :return: string
        """
        if self.status == Status.Infected:
            return "{}({})".format(self.status.name, self.infected_status.name)
        else:
            return self.status.name

    def __str__(self):
        return str(self.status.name)
