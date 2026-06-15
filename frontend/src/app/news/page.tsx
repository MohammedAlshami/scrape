"use client";

import { useState, useEffect } from "react";
import Image from "next/image";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";
import {
  Pagination,
  PaginationContent,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";
import { AspectRatio } from "@/components/ui/aspect-ratio";

const API = "";

interface NewsItem {
  title: string;
  url: string;
  summary: string | null;
  image_url: string | null;
  published_at: string | null;
}

interface ContentBlock {
  type: string;
  text: string;
  children?: string[];
  src?: string;
  alt?: string;
}

export default function NewsPage() {
  const [articles, setArticles] = useState<NewsItem[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [selected, setSelected] = useState<NewsItem | null>(null);
  const [content, setContent] = useState<ContentBlock[]>([]);
  const [loadingContent, setLoadingContent] = useState(false);

  useEffect(() => {
    fetch(`${API}/api/news/search?page=${page}`)
      .then(r => r.json())
      .then(data => {
        setArticles(data.articles);
        setTotalPages(data.totalPages);
      });
  }, [page]);

  const openArticle = async (article: NewsItem) => {
    setSelected(article);
    setContent([]);
    setLoadingContent(true);
    try {
      const r = await fetch(`${API}/api/news/article?url=${encodeURIComponent(article.url)}`);
      const data = await r.json();
      setContent(data.content || []);
    } catch {
    } finally {
      setLoadingContent(false);
    }
  };

  return (
    <div>
      <div className="max-w-7xl mx-auto px-4 pt-10">
        <div className="text-center mb-10">
          <h1 className="heading-lg mb-3">News</h1>
          <p className="text-muted-foreground text-lg">
            {totalPages > 0
              ? `Page ${page} of ${totalPages}`
              : "No articles found"}
          </p>
        </div>
      </div>

      {articles.length > 0 && (
        <>
          <div className="max-w-7xl mx-auto px-4">
            <div className="grid grid-cols-1 gap-8 md:grid-cols-2 md:gap-4 lg:grid-cols-4">
              {articles.map((a, i) => (
                <button
                  key={i}
                  onClick={() => openArticle(a)}
                  className="group block text-left w-full"
                >
                  <div className="flex flex-col gap-4 rounded-xl transition-all duration-200">
                    <AspectRatio ratio={4 / 3} className="overflow-hidden rounded-xl">
                      <Image
                        src={a.image_url || ""}
                        alt={a.title}
                        fill
                        className="h-full w-full object-cover transition-transform duration-200 group-hover:scale-105"
                      />
                    </AspectRatio>
                    <div className="flex flex-col gap-3">
                      <div className="flex items-center gap-2 text-left">
                        <span className="text-muted-foreground text-sm">
                          {a.published_at
                            ? new Date(a.published_at).toLocaleDateString("en-MY", {
                                year: "numeric", month: "short", day: "numeric",
                              })
                            : ""}
                        </span>
                      </div>
                      <h3 className="text-base font-semibold tracking-tight group-hover:underline line-clamp-2">
                        {a.title}
                      </h3>
                      {a.summary && (
                        <p className="text-muted-foreground text-sm line-clamp-2">
                          {a.summary}
                        </p>
                      )}
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>

          <div className="py-8">
            <Pagination>
              <PaginationContent>
                <PaginationItem>
                  <PaginationPrevious
                    href="#"
                    onClick={(e) => { e.preventDefault(); if (page > 1) setPage(p => p - 1); }}
                  />
                </PaginationItem>
                {Array.from({ length: Math.min(totalPages, 10) }, (_, i) => i + 1).map(p => (
                  <PaginationItem key={p}>
                    <PaginationLink
                      href="#"
                      isActive={p === page}
                      onClick={(e) => { e.preventDefault(); setPage(p); }}
                    >
                      {p}
                    </PaginationLink>
                  </PaginationItem>
                ))}
                <PaginationItem>
                  <PaginationNext
                    href="#"
                    onClick={(e) => { e.preventDefault(); if (page < totalPages) setPage(p => p + 1); }}
                  />
                </PaginationItem>
              </PaginationContent>
            </Pagination>
          </div>
        </>
      )}

      <Dialog open={!!selected} onOpenChange={(open) => { if (!open) setSelected(null); }}>
        <DialogContent className="sm:max-w-3xl lg:max-w-4xl max-h-[80vh] overflow-y-auto rounded-2xl scrollbar-hide p-0 gap-0">
          {selected && (
            <>
              {selected.image_url && (
                <div className="relative w-full h-56 md:h-72 rounded-t-2xl overflow-hidden">
                  <Image
                    src={selected.image_url}
                    alt={selected.title}
                    fill
                    className="object-cover"
                  />
                </div>
              )}
              <div className="p-5 space-y-4">
                <DialogHeader>
                  <DialogTitle className="text-xl leading-tight">{selected.title}</DialogTitle>
                  {selected.published_at && (
                    <DialogDescription>
                      {new Date(selected.published_at).toLocaleDateString("en-MY", {
                        year: "numeric", month: "long", day: "numeric",
                      })}
                    </DialogDescription>
                  )}
                </DialogHeader>

                {loadingContent && (
                  <p className="text-sm text-muted-foreground">Loading content…</p>
                )}

                {!loadingContent && content.length > 0 && (
                  <div className="space-y-4">
                    {content.map((block, i) => {
                      switch (block.type) {
                        case "h1":
                          return <h1 key={i} className="text-xl font-bold">{block.text}</h1>;
                        case "h2":
                          return <h2 key={i} className="text-lg font-semibold">{block.text}</h2>;
                        case "h3":
                          return <h3 key={i} className="text-base font-medium">{block.text}</h3>;
                        case "p":
                          return <p key={i} className="text-sm leading-relaxed text-muted-foreground">{block.text}</p>;
                        case "bold":
                          return <p key={i} className="text-sm font-semibold">{block.text}</p>;
                        case "italic":
                          return <p key={i} className="text-sm italic">{block.text}</p>;
                        case "blockquote":
                          return (
                            <blockquote key={i} className="border-l-2 pl-4 italic text-sm text-muted-foreground">
                              {block.text}
                            </blockquote>
                          );
                        case "ul":
                          return (
                            <ul key={i} className="list-disc pl-5 space-y-1 text-sm text-muted-foreground">
                              {(block.children || []).map((item, j) => (
                                <li key={j}>{item}</li>
                              ))}
                            </ul>
                          );
                        case "ol":
                          return (
                            <ol key={i} className="list-decimal pl-5 space-y-1 text-sm text-muted-foreground">
                              {(block.children || []).map((item, j) => (
                                <li key={j}>{item}</li>
                              ))}
                            </ol>
                          );
                        case "img":
                          return (
                            <div key={i} className="relative w-full h-48 my-2">
                              <Image
                                src={block.src || ""}
                                alt={block.alt || ""}
                                fill
                                className="object-contain"
                              />
                            </div>
                          );
                        default:
                          return null;
                      }
                    })}
                  </div>
                )}

                {!loadingContent && content.length === 0 && selected.summary && (
                  <p className="text-sm text-muted-foreground">{selected.summary}</p>
                )}
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
