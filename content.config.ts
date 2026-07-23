import { defineCollection, defineContentConfig } from '@nuxt/content'
import { z } from 'zod'

export default defineContentConfig({
  collections: {
    pogers: defineCollection({
      type: 'data',
      source: 'poger.csv',
      schema: z.object({
        index: z.number(),
        plid: z.string(),
        name: z.string(),
        pl_name: z.string(),
        description: z.string().optional(),
        url: z.string().url(),
        file_name: z.string(),
      })
    }),
    playlists: defineCollection({
      type: 'data',
      source: 'data/**.csv',
      schema: z.object({
        // Body is important in CSV files, without body field you cannot access to data array
        body: z.array(z.object({
          song: z.string(),
          song_url: z.string().url(),
          song_id: z.string(),
          artist: z.string(),
          artist_url: z.string().url(),
          album: z.string(),
          album_url: z.string().url(),
          stuwant: z.string(),
          stuwant_url: z.string().url(),
          duration: z.number(),
          timestamp: z.string().datetime(),
          file_name: z.string(),
        }))
      })
    })
  }
})
