import discord

from discord.ext.commands import command
from discord.ext.commands import Cog, Greedy
from discord.ext.commands import has_permissions, when_mentioned_or

from typing import Optional
import os
import threading
import requests
import random
import asyncio
import time
import sqlite3

from lib.db import db