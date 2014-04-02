from ..base import Result
from ..dns import DnsResult

def test_dns_4460():
    result = Result.get('{"af":4,"dst_addr":"193.227.234.53","from":"217.172.81.146","fw":4460,"msm_id":1004041,"prb_id":184,"proto":"UDP","result":{"ANCOUNT":1,"ARCOUNT":0,"ID":39825,"NSCOUNT":0,"QDCOUNT":1,"abuf":"m5GEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==","answers":[{"RDLENGTH":4,"TYPE":1}],"rt":45.305,"size":43},"timestamp":1347765990,"type":"dns"}')
    assert(isinstance(result, DnsResult))
    assert(result.origin == "217.172.81.146")
    assert(result.firmware == 4460)
    assert(result.measurement_id == 1004041)
    assert(result.probe_id == 184)
    assert(result.created.isoformat() == "2012-09-16T03:26:30+00:00")
    assert(isinstance(result.responses, list))
    assert(len(result.responses) == 1)
    assert(result.responses[0].af == 4)
    assert(result.responses[0].destination_address == "193.227.234.53")
    assert(result.responses[0].source_address is None)
    assert(result.responses[0].protocol == DnsResult.PROTOCOL_UDP)
    assert(result.responses[0].abuf == "m5GEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==")
    assert(result.responses[0].response_time == 45.305)
    assert(result.responses[0].response_size == 43)
    assert(result.responses[0].header.aa is True)
    assert(result.responses[0].header.qr is True)
    assert(result.responses[0].header.nscount == 0)
    assert(result.responses[0].header.qdcount == 1)
    assert(result.responses[0].header.ancount == 1)
    assert(result.responses[0].header.tc is False)
    assert(result.responses[0].header.rd is False)
    assert(result.responses[0].header.arcount == 0)
    assert(result.responses[0].header.return_code == "NOERROR")
    assert(result.responses[0].header.opcode == "QUERY")
    assert(result.responses[0].header.ra is False)
    assert(result.responses[0].header.z == 0)
    assert(result.responses[0].header.id == 39825)
    assert(isinstance(result.responses[0].questions, list))
    assert(result.responses[0].questions[0].klass == "IN")
    assert(result.responses[0].questions[0].type == "A")
    assert(result.responses[0].questions[0].name == "as250.net.")
    assert(isinstance(result.responses[0].answers, list))
    assert(result.responses[0].answers[0].name == "as250.net.")
    assert(result.responses[0].answers[0].ttl == 3600)
    assert(result.responses[0].answers[0].address == "194.150.168.100")
    assert(result.responses[0].answers[0].type == "A")
    assert(result.responses[0].answers[0].klass == "IN")
    assert(result.responses[0].answers[0].rd_length == 4)

def test_dns_4470():
    result = Result.get('{"af":4,"dst_addr":"193.227.234.53","from":"195.47.235.67","fw":4470,"msm_id":1004041,"prb_id":148,"proto":"UDP","result":{"ANCOUNT":1,"ARCOUNT":0,"ID":63020,"NSCOUNT":0,"QDCOUNT":1,"abuf":"9iyEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==","rt":30.733000000000001,"size":43},"src_addr":"195.47.235.67","timestamp":1352273196,"type":"dns"}')
    assert(isinstance(result, DnsResult))
    assert(result.origin == "195.47.235.67")
    assert(result.firmware == 4470)
    assert(result.measurement_id == 1004041)
    assert(result.probe_id == 148)
    assert(result.created.isoformat() == "2012-11-07T07:26:36+00:00")
    assert(isinstance(result.responses, list))
    assert(len(result.responses) == 1)
    assert(result.responses[0].af == 4)
    assert(result.responses[0].destination_address == "193.227.234.53")
    assert(result.responses[0].source_address == "195.47.235.67")
    assert(result.responses[0].protocol == DnsResult.PROTOCOL_UDP)
    assert(result.responses[0].abuf == "9iyEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==")
    assert(result.responses[0].response_time == 30.733)
    assert(result.responses[0].response_size == 43)
    assert(result.responses[0].header.aa is True)
    assert(result.responses[0].header.qr is True)
    assert(result.responses[0].header.nscount == 0)
    assert(result.responses[0].header.qdcount == 1)
    assert(result.responses[0].header.ancount == 1)
    assert(result.responses[0].header.tc is False)
    assert(result.responses[0].header.rd is False)
    assert(result.responses[0].header.arcount == 0)
    assert(result.responses[0].header.return_code == "NOERROR")
    assert(result.responses[0].header.opcode == "QUERY")
    assert(result.responses[0].header.ra is False)
    assert(result.responses[0].header.z == 0)
    assert(result.responses[0].header.id == 63020)
    assert(isinstance(result.responses[0].questions, list))
    assert(result.responses[0].questions[0].klass == "IN")
    assert(result.responses[0].questions[0].type == "A")
    assert(result.responses[0].questions[0].name == "as250.net.")
    assert(isinstance(result.responses[0].answers, list))
    assert(result.responses[0].answers[0].name == "as250.net.")
    assert(result.responses[0].answers[0].ttl == 3600)
    assert(result.responses[0].answers[0].address == "194.150.168.100")
    assert(result.responses[0].answers[0].type == "A")
    assert(result.responses[0].answers[0].klass == "IN")
    assert(result.responses[0].answers[0].rd_length == 4)

def test_dns_4480():
    result = Result.get('{"af":4,"dst_addr":"193.227.234.53","from":"46.17.16.18","fw":4480,"msm_id":1004041,"prb_id":778,"proto":"UDP","result":{"ANCOUNT":1,"ARCOUNT":0,"ID":12288,"NSCOUNT":0,"QDCOUNT":1,"abuf":"MACEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==","rt":38.576999999999998,"size":43},"src_addr":"192.168.1.12","timestamp":1363332374,"type":"dns"}')
    assert(isinstance(result, DnsResult))
    assert(result.origin == "46.17.16.18")
    assert(result.firmware == 4480)
    assert(result.measurement_id == 1004041)
    assert(result.probe_id == 778)
    assert(result.created.isoformat() == "2013-03-15T07:26:14+00:00")
    assert(isinstance(result.responses, list))
    assert(len(result.responses) == 1)
    assert(result.responses[0].af == 4)
    assert(result.responses[0].destination_address == "193.227.234.53")
    assert(result.responses[0].source_address == "192.168.1.12")
    assert(result.responses[0].protocol == DnsResult.PROTOCOL_UDP)
    assert(result.responses[0].abuf == "MACEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==")
    assert(result.responses[0].response_time == 38.577)
    assert(result.responses[0].response_size == 43)
    assert(result.responses[0].header.aa is True)
    assert(result.responses[0].header.qr is True)
    assert(result.responses[0].header.nscount == 0)
    assert(result.responses[0].header.qdcount == 1)
    assert(result.responses[0].header.ancount == 1)
    assert(result.responses[0].header.tc is False)
    assert(result.responses[0].header.rd is False)
    assert(result.responses[0].header.arcount == 0)
    assert(result.responses[0].header.return_code == "NOERROR")
    assert(result.responses[0].header.opcode == "QUERY")
    assert(result.responses[0].header.ra is False)
    assert(result.responses[0].header.z == 0)
    assert(result.responses[0].header.id == 12288)
    assert(isinstance(result.responses[0].questions, list))
    assert(result.responses[0].questions[0].klass == "IN")
    assert(result.responses[0].questions[0].type == "A")
    assert(result.responses[0].questions[0].name == "as250.net.")
    assert(isinstance(result.responses[0].answers, list))
    assert(result.responses[0].answers[0].name == "as250.net.")
    assert(result.responses[0].answers[0].ttl == 3600)
    assert(result.responses[0].answers[0].address == "194.150.168.100")
    assert(result.responses[0].answers[0].type == "A")
    assert(result.responses[0].answers[0].klass == "IN")
    assert(result.responses[0].answers[0].rd_length == 4)

def test_dns_4500():
    result = Result.get('{"af":4,"dst_addr":"193.227.234.53","from":"176.28.80.97","fw":4500,"msm_id":1004041,"prb_id":2918,"proto":"UDP","result":{"ANCOUNT":1,"ARCOUNT":0,"ID":57235,"NSCOUNT":0,"QDCOUNT":1,"abuf":"35OEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==","rt":69.736999999999995,"size":43},"src_addr":"10.220.3.215","timestamp":1366255550,"type":"dns"}')
    assert(isinstance(result, DnsResult))
    assert(result.origin == "176.28.80.97")
    assert(result.firmware == 4500)
    assert(result.measurement_id == 1004041)
    assert(result.probe_id == 2918)
    assert(result.created.isoformat() == "2013-04-18T03:25:50+00:00")
    assert(isinstance(result.responses, list))
    assert(len(result.responses) == 1)
    assert(result.responses[0].af == 4)
    assert(result.responses[0].destination_address == "193.227.234.53")
    assert(result.responses[0].source_address == "10.220.3.215")
    assert(result.responses[0].protocol == DnsResult.PROTOCOL_UDP)
    assert(result.responses[0].abuf == "35OEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaoZA==")
    assert(result.responses[0].response_time == 69.737)
    assert(result.responses[0].response_size == 43)
    assert(result.responses[0].header.aa is True)
    assert(result.responses[0].header.qr is True)
    assert(result.responses[0].header.nscount == 0)
    assert(result.responses[0].header.qdcount == 1)
    assert(result.responses[0].header.ancount == 1)
    assert(result.responses[0].header.tc is False)
    assert(result.responses[0].header.rd is False)
    assert(result.responses[0].header.arcount == 0)
    assert(result.responses[0].header.return_code == "NOERROR")
    assert(result.responses[0].header.opcode == "QUERY")
    assert(result.responses[0].header.ra is False)
    assert(result.responses[0].header.z == 0)
    assert(result.responses[0].header.id == 57235)
    assert(isinstance(result.responses[0].questions, list))
    assert(result.responses[0].questions[0].klass == "IN")
    assert(result.responses[0].questions[0].type == "A")
    assert(result.responses[0].questions[0].name == "as250.net.")
    assert(isinstance(result.responses[0].answers, list))
    assert(result.responses[0].answers[0].name == "as250.net.")
    assert(result.responses[0].answers[0].ttl == 3600)
    assert(result.responses[0].answers[0].address == "194.150.168.100")
    assert(result.responses[0].answers[0].type == "A")
    assert(result.responses[0].answers[0].klass == "IN")
    assert(result.responses[0].answers[0].rd_length == 4)

def test_dns_4520():
    result = Result.get('{"af":4,"dst_addr":"193.227.234.53","fw":4520,"msm_id":1004041,"prb_id":203,"proto":"UDP","result":{"ANCOUNT":1,"ARCOUNT":0,"ID":1472,"NSCOUNT":0,"QDCOUNT":1,"abuf":"BcCEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaooA==","rt":362.416,"size":43},"src_addr":"118.208.45.191","timestamp":1373241512,"type":"dns"}')
    assert(isinstance(result, DnsResult))
    assert(result.origin is None)
    assert(result.firmware == 4520)
    assert(result.measurement_id == 1004041)
    assert(result.probe_id == 203)
    assert(result.created.isoformat() == "2013-07-07T23:58:32+00:00")
    assert(isinstance(result.responses, list))
    assert(len(result.responses) == 1)
    assert(result.responses[0].af == 4)
    assert(result.responses[0].destination_address == "193.227.234.53")
    assert(result.responses[0].source_address == "118.208.45.191")
    assert(result.responses[0].protocol == DnsResult.PROTOCOL_UDP)
    assert(result.responses[0].abuf == "BcCEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaooA==")
    assert(result.responses[0].response_time == 362.416)
    assert(result.responses[0].response_size == 43)
    assert(result.responses[0].header.aa is True)
    assert(result.responses[0].header.qr is True)
    assert(result.responses[0].header.nscount == 0)
    assert(result.responses[0].header.qdcount == 1)
    assert(result.responses[0].header.ancount == 1)
    assert(result.responses[0].header.tc is False)
    assert(result.responses[0].header.rd is False)
    assert(result.responses[0].header.arcount == 0)
    assert(result.responses[0].header.return_code == "NOERROR")
    assert(result.responses[0].header.opcode == "QUERY")
    assert(result.responses[0].header.ra is False)
    assert(result.responses[0].header.z == 0)
    assert(result.responses[0].header.id == 1472)
    assert(isinstance(result.responses[0].questions, list))
    assert(result.responses[0].questions[0].klass == "IN")
    assert(result.responses[0].questions[0].type == "A")
    assert(result.responses[0].questions[0].name == "as250.net.")
    assert(isinstance(result.responses[0].answers, list))
    assert(result.responses[0].answers[0].name == "as250.net.")
    assert(result.responses[0].answers[0].ttl == 3600)
    assert(result.responses[0].answers[0].address == "194.150.168.160")
    assert(result.responses[0].answers[0].type == "A")
    assert(result.responses[0].answers[0].klass == "IN")
    assert(result.responses[0].answers[0].rd_length == 4)

def test_dns_4610():
    result = Result.get('{"af":4,"dst_addr":"193.227.234.53","from":"79.134.181.58","fw":4610,"msm_id":1004041,"msm_name":"Tdig","prb_id":714,"proto":"UDP","result":{"ANCOUNT":1,"ARCOUNT":0,"ID":15824,"NSCOUNT":0,"QDCOUNT":1,"abuf":"PdCEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaooA==","rt":81.718000000000004,"size":43},"result-rt":81.718000000000004,"src_addr":"192.168.0.100","timestamp":1395856407,"type":"dns"}')
    assert(isinstance(result, DnsResult))
    assert(result.origin == "79.134.181.58")
    assert(result.firmware == 4610)
    assert(result.measurement_id == 1004041)
    assert(result.probe_id == 714)
    assert(result.created.isoformat() == "2014-03-26T17:53:27+00:00")
    assert(isinstance(result.responses, list))
    assert(len(result.responses) == 1)
    assert(result.responses[0].af == 4)
    assert(result.responses[0].destination_address == "193.227.234.53")
    assert(result.responses[0].source_address == "192.168.0.100")
    assert(result.responses[0].protocol == DnsResult.PROTOCOL_UDP)
    assert(result.responses[0].abuf == "PdCEAAABAAEAAAAABWFzMjUwA25ldAAAAQABwAwAAQABAAAOEAAEwpaooA==")
    assert(result.responses[0].response_time == 81.718)
    assert(result.responses[0].response_size == 43)
    assert(result.responses[0].header.aa is True)
    assert(result.responses[0].header.qr is True)
    assert(result.responses[0].header.nscount == 0)
    assert(result.responses[0].header.qdcount == 1)
    assert(result.responses[0].header.ancount == 1)
    assert(result.responses[0].header.tc is False)
    assert(result.responses[0].header.rd is False)
    assert(result.responses[0].header.arcount == 0)
    assert(result.responses[0].header.return_code == "NOERROR")
    assert(result.responses[0].header.opcode == "QUERY")
    assert(result.responses[0].header.ra is False)
    assert(result.responses[0].header.z == 0)
    assert(result.responses[0].header.id == 15824)
    assert(isinstance(result.responses[0].questions, list))
    assert(result.responses[0].questions[0].klass == "IN")
    assert(result.responses[0].questions[0].type == "A")
    assert(result.responses[0].questions[0].name == "as250.net.")
    assert(isinstance(result.responses[0].answers, list))
    assert(result.responses[0].answers[0].name == "as250.net.")
    assert(result.responses[0].answers[0].ttl == 3600)
    assert(result.responses[0].answers[0].address == "194.150.168.160")
    assert(result.responses[0].answers[0].type == "A")
    assert(result.responses[0].answers[0].klass == "IN")
    assert(result.responses[0].answers[0].rd_length == 4)

def test_resultset():
    result = Result.get('{"from":"87.218.115.95","fw":4610,"msm_id":1004049,"msm_name":"Tdig","prb_id":13337,"resultset":[{"af":4,"dst_addr":"192.168.1.1","proto":"UDP","result":{"ANCOUNT":1,"ARCOUNT":6,"ID":19506,"NSCOUNT":6,"QDCOUNT":1,"abuf":"TDKBgAABAAEABgAGA3d3dwRyaXBlA25ldAAAAQABwAwAAQABAAAnsgAEwQAGi8AQAAIAAQAACTsADANuczMDbmljAmZyAMAQAAIAAQAACTsAEAZzbnMtcGIDaXNjA29yZwDAEAACAAEAAAk7AA0Ec2VjMQVhcG5pY8AVwBAAAgABAAAJOwAOA3ByaQdhdXRoZG5zwBDAEAACAAEAAAk7AA4GdGlubmllBGFyaW7AFcAQAAIAAQAACTsABwRzZWMzwHPAOgABAAEAASqyAATAhgAxwFIAAQABAAAZUgAEwAUEAcBuAAEAAQAAAW0ABMoMHTvAhwABAAEAAAk7AATBAAkFwKEAAQABAAAWlAAEx9QANcC7AAEAAQAACjcABMoMHIw=","rt":2.9939999999999998,"size":290},"src_addr":"192.168.1.2","subid":1,"submax":3,"time":1395792203},{"af":4,"dst_addr":"109.69.8.34","proto":"UDP","result":{"ANCOUNT":2,"ARCOUNT":15,"ID":25432,"NSCOUNT":7,"QDCOUNT":1,"abuf":"Y1iBgAABAAIABwAPA3d3dwRyaXBlA25ldAAAAQABwAwAAQABAAAnsAAEwQAGi8AMAC4AAQAAJ7AAnAABBQMAAFRgU1kk1VMxicVypgRyaXBlA25ldAAO4dloUjFkGWQKhb7ovCvAUn0NxHnxhCG/8PxtVf2+gUCxU1DAwP6mhazefe/B7Ecz5EVaF0WpbNUwhYOlEApMVgxd26DzrH7n99Yx8XN+mp/jts7MhoXrybZyh4NJ4Lwd/eAxCwp81ZAj7YDUX+EVtM+8c5h72C1XVfYb3Q/k98BMAAIAAQAACToADQRzZWMxBWFwbmljwFHATAACAAEAAAk6ABAGc25zLXBiA2lzYwNvcmcAwEwAAgABAAAJOgAOA3ByaQdhdXRoZG5zwEzATAACAAEAAAk6AAwDbnMzA25pYwJmcgDATAACAAEAAAk6AAcEc2VjM8DnwEwAAgABAAAJOgAOBnRpbm5pZQRhcmluwFHATAAuAAEAAA3RAJwAAgUCAAAOEFNZJNVTMYnFcqYEcmlwZQNuZXQAPVTDPwe6Z82fnZBvGzBGjFgX/CLRCE0Z6atTKBxqGAMbQzoqFMv+pfqjwe/wTEcIJnWqvPRGxnERAFYRpEi/Fjws7ELstYPOGUaY/GU8J0j0wJ6xJzr0gF8RYHKzvSwV2b2v2pJqCWYx0v03Mzv9UOXxE3Yj0WgSqKLsRckUDvDBMQABAAEAASqxAATAhgAxwTEAHAABAAEqsQAQIAEGYDAGAAEAAAAAAAEAAcEXAAEAAQAACToABMEACQXBFwAcAAEAAAk6ABAgAQZ8AOAAAAAAAAAAAAAFwOIAAQABAAABbAAEygwdO8DiABwAAQAAAWwAECABDcAgAQAKRggAAAAAAFnBSQABAAEAAAo2AATKDByMwUkAHAABAAAKNgAQIAENwAABAABHdwAAAAABQMD7AAEAAQAAGVEABMAFBAHA+wAcAAEAABlRABAgAQUAAC4AAAAAAAAAAAABwVwAAQABAAAWkgAEx9QANcFcABwAAQAAFpIAECABBQAAEwAAAAAAAMfUADXBMQAuAAEAASqxAJoAAQgDAAKjAFM4bf9TLyzfq04DbmljAmZyAAoIofy0bTrtF6fosXpt3PoQAQK2NStYRCEn/n6x+AqYbqeqh26q7gP94d2PeMAPV+sVRcY9ZgoRu2a7GmE4bxwzr3MlcAyv/MHiOU2f7eW0xDegtoL5GXnLgLx0+CvoG8lbiquEQNRxVNqQ2G4FdwvjYPnirfxmFKsW6YhTradrwTEALgABAAEqsQCaABwIAwACowBTObYgUzA3a6tOA25pYwJmcgBSd6DmR9159Y1jhnViTvqjnB0Tq0EjZVL2O5G8EiAgq4sYY2BtOL/zrM6/wohJ7hVBtPRWJ1xEf9WQsm/oZeJUThPp52GjB2fEboxJct/4k7i3wNZ6gN2krl1vNb5CrOiaVpDcdJMmZTkrua4LV4uB+buS0hvZ15D5KtODmgke8wAAKRAAAACAAAAA","rt":76.292000000000002,"size":1137},"src_addr":"192.168.1.2","subid":2,"submax":3,"time":1395792204},{"af":4,"dst_addr":"8.8.8.8","proto":"UDP","result":{"ANCOUNT":2,"ARCOUNT":1,"ID":34160,"NSCOUNT":0,"QDCOUNT":1,"abuf":"hXCBoAABAAIAAAABA3d3dwRyaXBlA25ldAAAAQABwAwAAQABAAAs2AAEwQAGi8AMAC4AAQAALNgAnAABBQMAAFRgU1kk1VMxicVypgRyaXBlA25ldAAO4dloUjFkGWQKhb7ovCvAUn0NxHnxhCG/8PxtVf2+gUCxU1DAwP6mhazefe/B7Ecz5EVaF0WpbNUwhYOlEApMVgxd26DzrH7n99Yx8XN+mp/jts7MhoXrybZyh4NJ4Lwd/eAxCwp81ZAj7YDUX+EVtM+8c5h72C1XVfYb3Q/k9wAAKQIAAACAAAAA","rt":79.971000000000004,"size":225},"src_addr":"192.168.1.2","subid":3,"submax":3,"time":1395792205}],"timestamp":1395792203,"type":"dns"}')
    assert(isinstance(result, DnsResult))
    assert(result.origin == "87.218.115.95")
    assert(result.firmware == 4610)
    assert(result.measurement_id == 1004049)
    assert(result.probe_id == 13337)
    assert(result.created.isoformat() == "2014-03-26T00:03:23+00:00")
    assert(isinstance(result.responses, list))
    assert(len(result.responses) == 3)
    assert(result.responses[0].af == 4)
    assert(result.responses[0].destination_address == "192.168.1.1")
    assert(result.responses[0].source_address == "192.168.1.2")
    assert(result.responses[0].protocol == DnsResult.PROTOCOL_UDP)
    assert(result.responses[0].abuf == "TDKBgAABAAEABgAGA3d3dwRyaXBlA25ldAAAAQABwAwAAQABAAAnsgAEwQAGi8AQAAIAAQAACTsADANuczMDbmljAmZyAMAQAAIAAQAACTsAEAZzbnMtcGIDaXNjA29yZwDAEAACAAEAAAk7AA0Ec2VjMQVhcG5pY8AVwBAAAgABAAAJOwAOA3ByaQdhdXRoZG5zwBDAEAACAAEAAAk7AA4GdGlubmllBGFyaW7AFcAQAAIAAQAACTsABwRzZWMzwHPAOgABAAEAASqyAATAhgAxwFIAAQABAAAZUgAEwAUEAcBuAAEAAQAAAW0ABMoMHTvAhwABAAEAAAk7AATBAAkFwKEAAQABAAAWlAAEx9QANcC7AAEAAQAACjcABMoMHIw=")
    assert(result.responses[0].response_time == 2.994)
    assert(result.responses[0].response_size == 290)
    assert(result.responses[0].header.aa is False)
    assert(result.responses[0].header.qr is True)
    assert(result.responses[0].header.nscount == 6)
    assert(result.responses[0].header.qdcount == 1)
    assert(result.responses[0].header.ancount == 1)
    assert(result.responses[0].header.tc is False)
    assert(result.responses[0].header.rd is True)
    assert(result.responses[0].header.arcount == 6)
    assert(result.responses[0].header.return_code == "NOERROR")
    assert(result.responses[0].header.opcode == "QUERY")
    assert(result.responses[0].header.ra is True)
    assert(result.responses[0].header.z == 0)
    assert(result.responses[0].header.id == 19506)
    assert(result.responses[1].header.id == 25432)
    assert(result.responses[2].header.id == 34160)
    assert(isinstance(result.responses[0].questions, list))
    assert(result.responses[0].questions[0].klass == "IN")
    assert(result.responses[0].questions[0].type == "A")
    assert(result.responses[0].questions[0].name == "www.ripe.net.")
    assert(result.responses[1].questions[0].type == "A")
    assert(result.responses[2].questions[0].name == "www.ripe.net.")
    assert(isinstance(result.responses[0].answers, list))
    assert(result.responses[0].answers[0].name == "www.ripe.net.")
    assert(result.responses[0].answers[0].ttl == 10162)
    assert(result.responses[0].answers[0].address == "193.0.6.139")
    assert(result.responses[0].answers[0].type == "A")
    assert(result.responses[0].answers[0].klass == "IN")
    assert(result.responses[0].answers[0].rd_length == 4)
    assert(result.responses[1].answers[1].rd_length == 156)
    assert(isinstance(result.responses[0].authorities, list))
    assert(len(result.responses[0].authorities) == 6)
    assert(result.responses[0].authorities[0].target == "ns3.nic.fr.")
    assert(result.responses[0].authorities[1].target == "sns-pb.isc.org.")
    assert(result.responses[0].authorities[2].target == "sec1.apnic.net.")
    assert(result.responses[0].authorities[3].target == "pri.authdns.ripe.net.")
    assert(result.responses[0].authorities[4].rd_length == 14)
    assert(result.responses[0].authorities[5].ttl == 2363)
    assert(result.responses[0].authorities[5].type == "NS")
    assert(result.responses[0].authorities[1].rd_length == 16)
    assert(result.responses[0].authorities[2].ttl == 2363)
    assert(result.responses[0].authorities[3].target == "pri.authdns.ripe.net.")
    assert(isinstance(result.responses[0].additionals, list))
    assert(len(result.responses[0].additionals) == 6)
    assert(result.responses[0].additionals[0].address == "192.134.0.49")
    assert(result.responses[0].additionals[1].klass == "IN")
    assert(result.responses[0].additionals[2].name == "sec1.apnic.net.")
    assert(result.responses[0].additionals[3].rd_length == 4)
    assert(result.responses[0].additionals[4].ttl == 5780)
    assert(result.responses[0].additionals[3].type == "A")
