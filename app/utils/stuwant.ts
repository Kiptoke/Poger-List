export default function (usercode: string) {
  const USER_TABLE: Record<string, string> = {
    'ka': 'Kaavya',
    'mu': 'Musa',
    'an': 'Andrew',
    'nt': 'Natasha',
    'nv': 'Naveen',
    'am': 'Aman',
    'ku': 'Kushal',
    'fa': 'Farah',
    're': 'Renny',
    'bi': 'Billy',
    'va': 'Val',
    'di': 'Dilan',
    'to': 'Tolu',
    'nd': 'Nadia',
    'ni': 'Nicholas',
  }
  return USER_TABLE[usercode]
}