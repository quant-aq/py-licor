import serial
from bs4 import BeautifulSoup as bs
import datetime

__all__ = ["Licor840"]

def safe_cast(value, cast):
    try:
        rv = cast(value)
    except:
        rv = None
    return rv

class Licor840:
    COLUMNS = [
        "timestamp",
        "cell_temp",
        "cell_pressure",
        "co2",
        "co2_abs",
        "h20",
        "h20_abs",
        "h20_dewpoint",
        "ivolt",
        "raw_co2",
        "raw_co2_ref",
        "raw_h20",
        "raw_h20_ref"
    ]

    def __init__(self, **kwargs):
        self.port = kwargs.pop("port", None)
        self.baud = kwargs.pop("baud", 9600)
        self.timeout = kwargs.pop("timeout", 2)

        self.con = None

    def connect(self):
        """
        """
        try:
            self.con = serial.Serial(
                self.port, self.baud, timeout=self.timeout)
        except:
            return False

        return True

    def read(self):
        """
        """
        if not self.con:
            raise Exception("Connection not setup.")

        # read the xml input
        raw = bs(self.con.readline(), "lxml")

        # make nice and pretty
        raw = raw.li840

        # merge to a dictionary
        if raw and raw.data:
            try:
                rv = [
                    datetime.datetime.utcnow().isoformat(),
                    float(raw.data.celltemp.string),
                    float(raw.data.cellpres.string),
                    float(raw.data.co2.string),
                    float(raw.data.co2abs.string),
                    float(raw.data.h2o.string),
                    float(raw.data.h2oabs.string),
                    float(raw.data.h2odewpoint.string),
                    float(raw.data.ivolt.string),
                    float(raw.data.raw.co2.string),
                    float(raw.data.raw.co2ref.string),
                    float(raw.data.raw.h2o.string),
                    float(raw.data.raw.h2oref.string)
                ]

                rv = dict(zip(self.COLUMNS, rv))
            except:
                rv = dict()

            return rv

        return dict()
